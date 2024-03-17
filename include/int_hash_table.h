#include <stdint.h>

typedef struct hashItem {
  uint16_t key;
  uint32_t value;
} HashItem;

typedef struct hashTable {
  uint16_t size;
  uint16_t maxSize;
  HashItem **hashItems;
} HashTable;

void freeHashTable(HashTable *hashTable);

HashTable *createHashTable(uint16_t size);

int8_t setHashItem(HashTable *hashTable, int16_t key, int32_t value);

HashItem *getHashItem(HashTable *hashTable, int16_t key);
