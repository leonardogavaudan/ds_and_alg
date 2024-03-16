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

HashTable *createHashTable(uint16_t maxSize);

void setHashItem(HashTable *hashTable, int16_t key, int32_t value);

int32_t getHashItemValue(HashTable *hashTable, int16_t key);
