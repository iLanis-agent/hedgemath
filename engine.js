// Hedge Math engine - hedge trimmer honesty, labeled norms, honest arithmetic.
// No cutting verdicts: what a blade can safely cut is the manufacturer's call.
// Only pass and schedule arithmetic here.
(function(root){
"use strict";
var GRIP = 3;      // labeled norm: inches of blade you cannot honestly work with
function r1(x){ return Math.round(x*10)/10; }
function f1(x){ return r1(x).toFixed(1); }

function bladePlan(bladeIn, heightFt){
  if (!(bladeIn > 0)) return { error: "the blade inches must be above zero" };
  if (!(heightFt > 0)) return { error: "the hedge feet must be above zero" };
  if (!(bladeIn > GRIP)) return { error: "the blade must be longer than the 3-inch grip norm" };
  var honestRaw = bladeIn - GRIP;
  var passes = Math.ceil(heightFt * 12 / honestRaw);
  var verdict = passes <= 2 ? "two honest sweeps" : (passes <= 5 ? "a working rhythm" : "a comb-over, not a haircut");
  return { honestIn: r1(honestRaw), passes: passes, verdict: verdict };
}
function renderBlade(r, bladeIn, heightFt){
  var passWord = r.passes === 1 ? "1 pass" : r.passes + " passes";
  return "The " + bladeIn + "-inch blade honestly works " + f1(r.honestIn) + " inches after the 3-inch grip norm; the " + heightFt + "-foot face is " + passWord + " - " + r.verdict + ".";
}

function hedgePlan(lengthFt, passes, paceFpm){
  if (!(lengthFt > 0)) return { error: "the hedge length must be above zero" };
  if (!(passes > 0)) return { error: "the passes per face must be above zero" };
  if (!(paceFpm > 0)) return { error: "the walking feet per minute must be above zero" };
  var minRaw = passes * lengthFt / paceFpm;
  var verdict = minRaw <= 20 ? "done before the coffee cools" : (minRaw <= 60 ? "a working morning" : "pack a lunch");
  return { minutes: r1(minRaw), verdict: verdict };
}
function renderHedge(r, lengthFt, passes, paceFpm){
  var passWord = passes === 1 ? "1 pass" : passes + " passes";
  var minWord = r.minutes === 1 ? "1 minute" : f1(r.minutes) + " minutes";
  return passWord + " down " + lengthFt + " feet at " + paceFpm + " feet a minute is " + minWord + " of trimming - " + r.verdict + ".";
}

root.HedgeMath = { bladePlan: bladePlan, renderBlade: renderBlade, hedgePlan: hedgePlan, renderHedge: renderHedge };
})(typeof window !== "undefined" ? window : globalThis);
