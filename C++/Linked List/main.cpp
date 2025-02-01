#include <iostream>

template <typename T>
struct SingleNode {
    T value;
    SingleNode* next;
};

template <typename T>
struct DoubleNode {
    T value;
    DoubleNode* next;
    DoubleNode* prev;
};

template <typename T>
class SinglyLinkedList {
   private:
    SingleNode<T>* head_ = nullptr;
    SingleNode<T>* tail_ = nullptr;

   public:
    SinglyLinkedList(T value) {
        SingleNode<T>* node = new SingleNode<T>();
        node->value = value;
        node->next = nullptr;

        this->head_ = node;
        this->tail_ = node;
    }

    ~SinglyLinkedList() {
        SingleNode<T>* current = this->head_;

        while (current) {
            SingleNode<T>* temp = current;
            current = current->next;
            delete temp;
        }
    }

    void Append(T value) {
        SingleNode<T>* node = new SingleNode<T>();
        node->value = value;
        node->next = nullptr;

        if (!this->tail_) {
            this->head_ = node;
            this->tail_ = node;
        } else {
            this->tail_->next = node;
            this->tail_ = node;
        }
    }

    void Prepend(T value) {
        SingleNode<T>* node = new SingleNode<T>();
        node->value = value;
        node->next = nullptr;

        if (!this->head_) {
            this->head_ = node;
            this->tail_ = node;
        } else {
            node->next = this->head_;
            this->head_ = node;
        }
    }

    void Insert(int index, T value) {
        if (index < 0) {
            throw std::runtime_error(
                "Index error: Insertion index cannot be less than zero.");
        }
        if (index == 0) {
            Prepend(value);
            return;
        }

        SingleNode<T>* current = this->head_;
        if (!current) {
            throw std::runtime_error("Index error: Out of range.");
        }

        int i = 0;
        int insert_index = index - 1;
        while (current) {
            if (i == insert_index) {
                SingleNode<T>* node = new SingleNode<T>();
                node->value = value;
                node->next = current->next;
                current->next = node;

                if (node->next == nullptr) {
                    this->tail_ = node;
                }

                return;
            }
            current = current->next;
            i++;
        }

        if (i + 1 == index) {
            Append(value);
            return;
        }

        throw std::runtime_error("Index error: Out of range.");
    }

    void Clear() {
        SingleNode<T>* current = this->head_;

        while (current) {
            SingleNode<T>* temp = current;
            current = current->next;
            delete temp;
        }

        this->head_ = nullptr;
        this->tail_ = nullptr;
    }
    // contains()
    // []
    // removeAt()
    // removeHead()
    // removeTail()
    // remove()
    T Head() {
        if (!this->head_) {
            throw std::runtime_error("List is empty.");
        }
        return this->head_->value;
    }

    T Tail() {
        if (!this->tail_) {
            throw std::runtime_error("List is empty.");
        }
        return this->tail_->value;
    }

    void PrintAll() {
        SingleNode<T>* current = this->head_;
        while (current) {
            std::cout << current->value << " -> ";
            current = current->next;
        }
        std::cout << "nullptr" << std::endl;
    }
};

int main() {
    SinglyLinkedList<int> list(10);
    list.Prepend(5);
    list.Append(20);

    list.Insert(3, 30);  // Inserts `30` at the last valid index (works!)
    list.PrintAll();     // Expected: 5 -> 10 -> 20 -> 30 -> nullptr

    list.Insert(5, 40);  // Should now APPEND instead of erroring
    list.PrintAll();     // Expected: 5 -> 10 -> 20 -> 30 -> 40 -> nullptr

    try {
        list.Insert(7, 50);  // Should throw "Out of range" (correct behavior)
        list.PrintAll();     // Shouldn't ever get here
    } catch (std::runtime_error& error) {
        list.PrintAll();  // Expected: 5 -> 10 -> 20 -> 30 -> 40 -> nullptr
    }

    return 0;
}