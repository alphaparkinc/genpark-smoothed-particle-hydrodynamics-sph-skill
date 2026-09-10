import sys
import json
from client import SPHFluidSimulator

sph = SPHFluidSimulator()

def handle_call(name, arguments):
    if name == "compute":
        pts = [tuple(p) for p in arguments["particles"]]
        t_idx = arguments.get("target_idx", 0)
        d, p = sph.compute_density_pressure(pts, t_idx)
        return {"density": d, "pressure": p}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
