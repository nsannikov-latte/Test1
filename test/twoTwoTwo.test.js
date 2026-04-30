import { test } from "node:test";
import assert from "node:assert/strict";
import { twoTwoTwo } from "../src/twoTwoTwo.js";

test("twoTwoTwo returns 222", () => {
  assert.equal(twoTwoTwo(), 222);
});
