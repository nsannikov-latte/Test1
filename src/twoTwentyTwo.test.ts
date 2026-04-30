import { describe, expect, it } from "vitest";
import { twoTwentyTwo } from "./twoTwentyTwo.js";

describe("twoTwentyTwo", () => {
  it("returns 222", () => {
    expect(twoTwentyTwo()).toBe(222);
  });
});
