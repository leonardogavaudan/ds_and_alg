#include <stdlib.h>

typedef enum {
  HT_STATUS_OK = 0,
  HT_STATUS_ALLOC_ERROR,
  HT_STATUS_RESIZE_ERROR,
} HashTableStatus;

const size_t INITIAL_HASH_TABLE_SIZE = 10;
const float MAX_LOAD_FACTOR = 0.75;

typedef struct Node {
  int key;
  int value;
  struct Node *next;
} Node;

typedef struct {
  Node **arr;
  size_t current_size;
  size_t max_size;
} HashTable;

void free_hash_table(HashTable *hash_table) {
  if(hash_table == NULL) {
    return;
  }

  for (size_t i = 0; i < hash_table->max_size; i++) {
    Node *node = hash_table->arr[i];
    while (node != NULL) {
      Node *temp = node->next;
      free(node);
      node = temp;
    }
  }
  free(hash_table->arr);
  free(hash_table);
}

HashTable *create_new_hash_table(size_t size) {
  if (size == 0) {
    return NULL;
  }

  HashTable *hash_table = malloc(sizeof(HashTable));
  if (hash_table == NULL) {
    return NULL;
  }

  Node **arr = malloc(size * sizeof(Node *));
  if (arr == NULL) {
    free(hash_table);
    return NULL;
  }
  hash_table->arr = arr;

  for (size_t i = 0; i < size; i++) {
    hash_table->arr[i] = NULL;
  }

  hash_table->current_size = 0;
  hash_table->max_size = size;

  return hash_table;
}

size_t hash(int key, size_t hash_table_max_size) {
  int rem = key % hash_table_max_size;
  if (rem < 0) {
    rem += hash_table_max_size;
  }
  return (size_t)rem;
}

HashTableStatus resize_hash_table(HashTable **hash_table_ref);

HashTableStatus set_item(HashTable **hash_table_ref, int key, int value) {
  HashTable *hash_table = *hash_table_ref;

  if ((double)(hash_table->current_size + 1) / hash_table->max_size > MAX_LOAD_FACTOR) {
    HashTableStatus code = resize_hash_table(hash_table_ref);
    if (code != HT_STATUS_OK) {
      return HT_STATUS_RESIZE_ERROR;
    }
  }

  hash_table = *hash_table_ref;

  size_t bucket_index = hash(key, hash_table->max_size);
  Node *node = hash_table->arr[bucket_index];
  Node *prev = NULL;
  while (node != NULL) {
    if (node->key == key) {
      node->value = value;
      return HT_STATUS_OK;
    }
    prev = node;
    node = node->next;
  }

  Node *new_node = malloc(sizeof(Node));
  if (new_node == NULL) {
    return HT_STATUS_ALLOC_ERROR;
  }
  new_node->key = key;
  new_node->value = value;
  new_node->next = NULL;

  hash_table->current_size++;


  if (prev == NULL) {
    hash_table->arr[bucket_index] = new_node;
  } else {
    prev->next = new_node;
  }

  return HT_STATUS_OK;
}

HashTableStatus resize_hash_table(HashTable **hash_table_ref) {
  HashTable *hash_table = *hash_table_ref;
  size_t new_max_size = 2 * hash_table->max_size;
  HashTable *new_hash_table = create_new_hash_table(new_max_size);
  if (new_hash_table == NULL) {
    return HT_STATUS_ALLOC_ERROR;
  }

  for (size_t i = 0; i < hash_table->max_size; i++) {
    Node *node = hash_table->arr[i];
    Node *next = NULL;
    while (node != NULL) {
      next = node->next;
      HashTableStatus code = set_item(&new_hash_table, node->key, node->value);
      if (code != HT_STATUS_OK) {
        free_hash_table(new_hash_table);
        return HT_STATUS_RESIZE_ERROR;
      }
      node = next;
    }
  }

  free_hash_table(hash_table);
  *hash_table_ref = new_hash_table;

  return HT_STATUS_OK;
}
