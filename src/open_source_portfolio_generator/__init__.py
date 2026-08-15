import argparse,hashlib,json
def generate(profile):
 repos=profile.get("repositories") if isinstance(profile,dict) else None
 if not isinstance(repos,list) or len(repos)>500:return {"ok":False,"errors":["invalid_repositories"]}
 if any(not isinstance(r,dict) or r.get("visibility")!="public" for r in repos):return {"ok":False,"errors":["non_public_repository"]}
 names=[r.get("name") for r in repos]
 if any(not isinstance(n,str) or not n for n in names) or len(names)!=len(set(names)):return {"ok":False,"errors":["invalid_or_duplicate_name"]}
 ordered=sorted(repos,key=lambda r:(-int(r.get("stars",0)),r["name"]));lines=[f"# {profile.get('display_name','Open-source portfolio')}",""]
 for r in ordered:lines.extend([f"## {r['name']}",str(r.get("description","")),f"Stars: {int(r.get('stars',0))}",""])
 body="\n".join(lines);return {"ok":True,"markdown":body,"repository_count":len(ordered),"sha256":hashlib.sha256(body.encode()).hexdigest()}
def probe():
 g=generate({"repositories":[{"name":"demo","visibility":"public"}]});b=generate({"repositories":[{"name":"secret","visibility":"private"}]});return {"ok":g["ok"] and not b["ok"],"private_counter_proof":not b["ok"]}
def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument("command",choices=("generate","probe"));p.add_argument("--input");a=p.parse_args(argv);o=probe() if a.command=="probe" else generate(json.load(open(a.input)));print(json.dumps(o,sort_keys=True));return 0 if o["ok"] else 2
