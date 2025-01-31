#include <iostream>

template <typename T>
class Node {
    public:
        T value;
        Node* next;

        Node(T value) {
            this->value = value;
            this->next = NULL;
        }
};

template <typename T>
class LinkedList {
    public:
        Node<T>* head;
        Node<T>* current;

        LinkedList(T value) {
            Node<T>* node = new Node<T>(value);
            this->head = node;
            this->current = NULL;
        }

        void add(T value) {
            Node<T>* node = new Node<T>(value);
            this->current = this->head;
            while (this->current->next != NULL) {
                this->current = this->current->next;
            }
            this->current->next = node;

            return;
        }

};

int main() {
    LinkedList list = LinkedList(5);
    list.add(10);
    list.add(20);

    list.current = list.head;
    while (list.current->next != NULL) {
        std::cout << list.current->value << std::endl;
        list.current = list.current->next;
    }
    std::cout << list.current->value << std::endl;

    return 0;
}