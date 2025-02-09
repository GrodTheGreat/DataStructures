class TsArray {
  constructor() {}
  //   Basics
  get<T>(index: number): T {}
  set<T>(index: number, value: T): void {}
  length(): number {}
  // insert<T>(index: number, value: T): void {}
  append<T>(value: T): void {}
  remove(index: number): void {}
  resize(newCapacity: number): void {}
  // //   Memory Management
  // shrinkToFit(): void {}
  // capacity(): number {}
  // swap<T>(index: number, jndex: number): this {}
  // fill<T>(value: T): this {}
  // copy(): TsArray {}
  // // Utility
  // first() {}
  // last() {}
  // isEmpty(): boolean {}
  // reverse(): this {}
  // clear(): this {}
  // clone(): TsArray {}
  // // Search
  // contains<T>(value: T): boolean {}
  // indexOf<T>(value: T): number {}
  // lastIndexOf() {}
  // binarySearch() {}
  // // Sorting
  // sort(): void {}
  // sortDescending() {}
  // shuffle() {}
  // // Functional
  // //   map(func: ): void {} //Hmmm...
  // //   filter(func: ): void {} //Hmmm...
  // // reduce(func: , initial) {} //Hmmm...
  // // flatMap() {} //Hmmm...
  // // forEach() {} //Hmmm...
  // // Partitioning
  // slice<T>(start: number, end: number): Array<T> {}
  // splice() {}
  // partition() {}
  // // Stack/Queue
  // push(value) {}
  // pop() {}
  // unshift(value) {}
  // shift() {}
  // rotate(shiftValue) {}
  // // Set
  // unique() {}
  // union(other: TsArray) {}
  // intersection(other: TsArray) {}
  // difference(other: TsArray) {}
  // // Math
  // sum() {}
  // product() {}
  // min() {}
  // max() {}
  // average() {}
  // median() {}
  // mode() {}
  // // Multidimensional
  // // get //Hmmm...
  // // set //Hmmm...
  // // transpose //Hmmm...
  // // flatten //Hmmm...
}
