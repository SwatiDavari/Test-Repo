#include "communication/serializer.h"
#include <string.h>

size_t serializer_encoded_size(const message_t *msg) {
    return sizeof(int) + sizeof(size_t) + msg->payload_len;
}

size_t serializer_encode(const message_t *msg, unsigned char *out_buf, size_t out_buf_size) {
    size_t needed = serializer_encoded_size(msg);
    if (out_buf_size < needed) {
        return 0;
    }

    size_t offset = 0;
    memcpy(out_buf + offset, &msg->topic_id, sizeof(int));
    offset += sizeof(int);
    memcpy(out_buf + offset, &msg->payload_len, sizeof(size_t));
    offset += sizeof(size_t);
    memcpy(out_buf + offset, msg->payload, msg->payload_len);
    offset += msg->payload_len;
    return offset;
}

int serializer_decode(const unsigned char *buf, size_t buf_size, message_t *out_msg) {
    if (buf_size < sizeof(int) + sizeof(size_t)) {
        return 0;
    }

    size_t offset = 0;
    int topic_id;
    memcpy(&topic_id, buf + offset, sizeof(int));
    offset += sizeof(int);

    size_t payload_len;
    memcpy(&payload_len, buf + offset, sizeof(size_t));
    offset += sizeof(size_t);

    if (buf_size - offset < payload_len) {
        return 0;
    }

    out_msg->topic_id = topic_id;
    out_msg->payload = (const char *)(buf + offset);
    out_msg->payload_len = payload_len;
    return 1;
}
