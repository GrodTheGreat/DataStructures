import { StaticArray } from "../src/StaticArray";

describe("StaticArray", () => {
  let arr: StaticArray<number>;

  beforeEach(() => {
    arr = new StaticArray<number>(5);
  });

  test("should initialize with a capacity of 5", () => {
    expect(arr.length()).toBe(5);
  });
});
