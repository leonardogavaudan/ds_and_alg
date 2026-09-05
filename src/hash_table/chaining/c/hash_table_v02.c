typedef struct Node {
    void *key;
    void *value;
    struct Node *next;
} Node;

typedef struct HashTable {
    int bucket_size;
    Node **bucket;
    int node_count;
} HashTable;

HashTable* create_hash_table() {
}