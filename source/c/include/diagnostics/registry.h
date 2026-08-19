#ifndef DIAGNOSTICS_REGISTRY_H
#define DIAGNOSTICS_REGISTRY_H

#include <stddef.h>

/* Implements UNIT_Z_001 (Service Registry Unit) —
 * needs/diagnostics/unit design/unit_z_001.rst:
 * "the in-memory registry of advertised service instances."
 *
 * Scenario matches needs/diagnostics/unit test/test procedures/PROC_UNIT_Z_001.yml
 * and needs/diagnostics/unit test/test cases/case_z_001.md
 * (TC_UNIT_Z_001): advertise, lookup-by-type returns all matching
 * instances side by side, withdraw removes an instance from subsequent
 * lookups. */

#define REGISTRY_MAX_INSTANCES 16

typedef struct {
    int instance_id;
    const char *service_type;
} service_instance_t;

typedef struct {
    service_instance_t instances[REGISTRY_MAX_INSTANCES];
    size_t count;
} service_registry_t;

/* Constructs reg with no advertised instances (per TCOND_UNIT_Z_001). */
void registry_init(service_registry_t *reg);

/* Advertises instance_id for service_type. Returns 1 on success, 0 if the
 * registry is full (REGISTRY_MAX_INSTANCES already advertised). */
int registry_advertise(service_registry_t *reg, int instance_id, const char *service_type);

/* Withdraws instance_id. Returns 1 if it was found and removed, 0 if no
 * such instance was advertised. */
int registry_withdraw(service_registry_t *reg, int instance_id);

/* Looks up all currently-advertised instances for service_type, writing
 * their instance ids into out_instance_ids (capacity out_capacity, in
 * advertise order). Returns the number of matching instances found
 * (which may exceed out_capacity — only the first out_capacity ids are
 * written in that case). */
size_t registry_lookup(const service_registry_t *reg, const char *service_type,
                        int *out_instance_ids, size_t out_capacity);

#endif /* DIAGNOSTICS_REGISTRY_H */
