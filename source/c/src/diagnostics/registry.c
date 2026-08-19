#include "diagnostics/registry.h"
#include <string.h>

void registry_init(service_registry_t *reg) {
    reg->count = 0;
}

int registry_advertise(service_registry_t *reg, int instance_id, const char *service_type) {
    if (reg->count >= REGISTRY_MAX_INSTANCES) {
        return 0;
    }
    reg->instances[reg->count].instance_id = instance_id;
    reg->instances[reg->count].service_type = service_type;
    reg->count += 1;
    return 1;
}

int registry_withdraw(service_registry_t *reg, int instance_id) {
    for (size_t i = 0; i < reg->count; i++) {
        if (reg->instances[i].instance_id == instance_id) {
            /* shift the remaining instances down to close the gap */
            for (size_t j = i; j + 1 < reg->count; j++) {
                reg->instances[j] = reg->instances[j + 1];
            }
            reg->count -= 1;
            return 1;
        }
    }
    return 0;
}

size_t registry_lookup(const service_registry_t *reg, const char *service_type,
                        int *out_instance_ids, size_t out_capacity) {
    size_t found = 0;
    for (size_t i = 0; i < reg->count; i++) {
        if (strcmp(reg->instances[i].service_type, service_type) == 0) {
            if (found < out_capacity) {
                out_instance_ids[found] = reg->instances[i].instance_id;
            }
            found += 1;
        }
    }
    return found;
}
