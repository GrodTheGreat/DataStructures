export class StaticArray<T> {
  private arr: Array<T>;
  private capacity: number;

  constructor(size: number) {
    this.capacity = size;
    this.arr = new Array(this.capacity);
  }
  get(index: number): T {
    return this.arr[index];
  }
  set(index: number, value: T): void {
    this.arr[index] = value;
  }
  length(): number {
    return this.capacity;
  }
  remove(index: number): this {
    delete this.arr[index];
    return this;
  }
}
