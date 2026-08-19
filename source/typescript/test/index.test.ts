import { describe, expect, it } from "vitest";
import { add } from "../src/index";

describe("add", () => {
  it("adds two positive numbers", () => {
    expect(add(2, 3)).toBe(5);
  });

  it("adds a negative and a positive number", () => {
    expect(add(-1, 1)).toBe(0);
  });

  it("adds two zeros", () => {
    expect(add(0, 0)).toBe(0);
  });

  it("is commutative", () => {
    expect(add(4, 7)).toBe(add(7, 4));
  });
});
