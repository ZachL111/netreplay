import assert from "node:assert/strict";
import { domainReviewLane, domainReviewScore } from "../src/domainReview.js";

const item = { signal: 66, slack: 47, drag: 21, confidence: 90 };
assert.equal(domainReviewScore(item), 206);
assert.equal(domainReviewLane(item), "ship");
