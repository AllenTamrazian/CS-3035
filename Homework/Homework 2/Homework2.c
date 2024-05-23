#include <stdio.h>
#include <stdlib.h>

struct node {
    int value;
    struct node* link;
};

struct node* addNode(int value, struct node* last) {
    struct node* newNode = (struct node*)malloc(sizeof(struct node));
  
    newNode->value = value;
    newNode->link = NULL;

    if (last == NULL) {
        return newNode;
    } else {
        last->link = newNode;
        return newNode;
    }
}

void printList(struct node* first) {
    struct node* current = first;
    while (current != NULL) {
        printf("%d ", current->value);
        current = current->link;
    }
    printf("\n");
}

void searchValue(int key, struct node* first) {
    struct node* current = first;
    while (current != NULL) {
        if (current->value == key) {
            printf("%d found in the list\n", key);
            return;
        }
        current = current->link;
    }
    printf("%d not found in the list\n", key);
}

int main() {
    struct node* firstNode = NULL;
    struct node* lastNode = NULL;

    lastNode = addNode(5, lastNode);
    if (firstNode == NULL) {
        firstNode = lastNode;
    }
    lastNode = addNode(10, lastNode);
    lastNode = addNode(15, lastNode);
    printList(firstNode);
    searchValue(10, firstNode);
    searchValue(20, firstNode);

    struct node* emptyListFirst = NULL;
    searchValue(30, emptyListFirst);
    
    return 0;
}
