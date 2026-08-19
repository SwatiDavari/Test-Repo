#ifndef COMMUNICATION_SERIALIZER_H
#define COMMUNICATION_SERIALIZER_H

#include <stddef.h>

/* Implements UNIT_A_001 (Proxy Serialization Unit) —
 * needs/communication/component/unit design/unit_a_001.rst:
 * "serialization and deserialization of messages within the proxy layer." */

typedef struct {
    int topic_id;
    const char *payload;
    size_t payload_len;
} message_t;

/* Exact number of bytes serializer_encode() would write for msg. */
size_t serializer_encoded_size(const message_t *msg);

/* Serializes msg into out_buf (caller-provided, at least
 * serializer_encoded_size(msg) bytes). Returns bytes written, or 0 if
 * out_buf is too small. */
size_t serializer_encode(const message_t *msg, unsigned char *out_buf, size_t out_buf_size);

/* Deserializes a message previously written by serializer_encode() from
 * buf (buf_size bytes). On success, populates *out_msg (out_msg->payload
 * points into buf — valid only as long as buf is) and returns 1. Returns
 * 0 on truncated/malformed input. */
int serializer_decode(const unsigned char *buf, size_t buf_size, message_t *out_msg);

#endif /* COMMUNICATION_SERIALIZER_H */
