import assert from "node:assert/strict";
import { classify, score } from "../src/policy.js";

const cases = [
  {
    "name": "case_1",
    "demand": 52,
    "capacity": 82,
    "latency": 8,
    "risk": 25,
    "weight": 13,
    "score": 47,
    "decision": "review"
  },
  {
    "name": "case_2",
    "demand": 63,
    "capacity": 82,
    "latency": 13,
    "risk": 9,
    "weight": 12,
    "score": 167,
    "decision": "accept"
  },
  {
    "name": "case_3",
    "demand": 73,
    "capacity": 91,
    "latency": 10,
    "risk": 21,
    "weight": 5,
    "score": 90,
    "decision": "review"
  }
];

for (const item of cases) {
  const signal = {
    demand: item.demand,
    capacity: item.capacity,
    latency: item.latency,
    risk: item.risk,
    weight: item.weight
  };
  assert.equal(score(signal), item.score);
  assert.equal(classify(signal), item.decision);
}
