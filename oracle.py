#!/usr/bin/env python3
# Hedge Math oracle - mirrors engine.js float-for-float.
import json, math
GRIP = 3
TOOTH = 0.8
def r1(x): return math.floor(x*10+0.5)/10
def f1(x): return "%.1f" % r1(x)
def jsnum(x):
    i = int(x)
    return i if x == i else x

def blade_plan(blade, height):
    if not (blade > 0): return {"error": "the blade inches must be above zero"}
    if not (height > 0): return {"error": "the hedge feet must be above zero"}
    if not (blade > GRIP): return {"error": "the blade must be longer than the 3-inch grip norm"}
    honest_raw = blade - GRIP
    passes = math.ceil(height * 12 / honest_raw)
    verdict = "two honest sweeps" if passes <= 2 else ("a working rhythm" if passes <= 5 else "a comb-over, not a haircut")
    return {"honestIn": jsnum(r1(honest_raw)), "passes": passes, "verdict": verdict}
def render_blade(r, blade, height):
    pass_word = "1 pass" if r["passes"] == 1 else "%s passes" % r["passes"]
    return ("The %s-inch blade honestly works %s inches after the 3-inch grip norm; the %s-foot face is %s - %s."
            % (blade, f1(r["honestIn"]), height, pass_word, r["verdict"]))

def hedge_plan(length, passes, pace):
    if not (length > 0): return {"error": "the hedge length must be above zero"}
    if not (passes > 0): return {"error": "the passes per face must be above zero"}
    if not (pace > 0): return {"error": "the walking feet per minute must be above zero"}
    min_raw = passes * length / pace
    verdict = "done before the coffee cools" if min_raw <= 20 else ("a working morning" if min_raw <= 60 else "pack a lunch")
    return {"minutes": jsnum(r1(min_raw)), "verdict": verdict}
def render_hedge(r, length, passes, pace):
    pass_word = "1 pass" if passes == 1 else "%s passes" % passes
    min_word = "1 minute" if r["minutes"] == 1 else f1(r["minutes"]) + " minutes"
    return ("%s down %s feet at %s feet a minute is %s of trimming - %s."
            % (pass_word, length, pace, min_word, r["verdict"]))

def tooth_plan(gap, branch):
    if not (gap > 0): return {"error": "the tooth gap must be above zero"}
    if not (branch > 0): return {"error": "the branch inches must be above zero"}
    honest_raw = gap * TOOTH
    verdict = "scissors clean" if branch <= honest_raw else ("chews but finishes" if branch <= gap else "is a lopper's branch, not the blade's")
    return {"honestIn": jsnum(r1(honest_raw)), "verdict": verdict}
def render_tooth(r, gap, branch):
    return ("The %s-inch gap honestly scissors %s inches at the 0.8 norm; the %s-inch branch %s."
            % (gap, f1(r["honestIn"]), branch, r["verdict"]))

CASES = [
    ("blade", (24,4)), ("blade", (22,2)), ("blade", (18,6)),
    ("blade", (16,8)), ("blade", (26,3)), ("blade", (20,5)),
    ("hedge", (30,3,20)), ("hedge", (60,4,15)), ("hedge", (100,3,25)),
    ("hedge", (80,8,20)), ("hedge", (150,4,18)), ("hedge", (200,8,15)),
    ("tooth", (0.75,0.5)), ("tooth", (0.75,0.7)), ("tooth", (0.75,1)),
    ("tooth", (1,0.8)), ("tooth", (0.6,0.4)), ("tooth", (1.2,1.5)),
    ("blade", (0,4)), ("blade", (24,0)),
    ("hedge", (0,3,20)), ("hedge", (30,0,20)), ("hedge", (30,3,0)),
    ("tooth", (0,0.5)), ("tooth", (0.75,0)),
]
PLANS = {"blade": (blade_plan, render_blade), "hedge": (hedge_plan, render_hedge), "tooth": (tooth_plan, render_tooth)}
out = []
for tool, args in CASES:
    plan, render = PLANS[tool]
    r = plan(*args)
    case = {"tool": tool, "args": list(args), "result": r}
    if "error" not in r:
        case["render"] = render(r, *args)
    out.append(case)
print(json.dumps(out, separators=(",", ":")), end="")
