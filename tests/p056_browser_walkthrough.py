"""P05.6 synthetic-data browser walkthrough. No production deployment."""
import json
import subprocess
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
DEMO=ROOT/"prototype"/"p055"
SHOTS=ROOT/"qualification"/"p056-browser-evidence"

def run():
    SHOTS.mkdir(parents=True,exist_ok=True)
    subprocess.run([sys.executable,"-m","protect_q01_p01.integrated_dashboard_demo",
                    str(DEMO/"synthetic-integrated.json")],cwd=ROOT,check=True)
    server=subprocess.Popen([sys.executable,"-m","http.server","8765","--bind","127.0.0.1"],
                            cwd=DEMO,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    results=[]
    try:
        with sync_playwright() as p:
            browser=p.chromium.launch(headless=True)
            for name,viewport in [("desktop",{"width":1440,"height":900}),("mobile",{"width":390,"height":844})]:
                page=browser.new_page(viewport=viewport,device_scale_factor=1)
                errors=[]
                page.on("pageerror",lambda err:errors.append(str(err)))
                for attempt in range(25):
                    try:
                        page.goto("http://127.0.0.1:8765/",wait_until="networkidle",timeout=4000)
                        break
                    except Exception:
                        if attempt==24:raise
                        time.sleep(.2)
                page.get_by_role("status").get_by_text("Synthetic integrated dashboard loaded.",exact=False).wait_for(timeout=10000)
                assert page.locator("#deviations").inner_text()=="2"
                assert page.locator("#capas").inner_text()=="1"
                assert page.locator("#reviews").inner_text()=="2"
                assert page.locator("#modules button").count()==13
                assert "SYNTHETIC PILOT" in page.locator(".notice").inner_text()
                page.screenshot(path=str(SHOTS/f"{name}-overview.png"),full_page=True)
                page.locator('button[data-code="Q03"]').click()
                assert "Not implemented" in page.locator("#sectionDescription").inner_text()
                assert page.locator('button[data-code="Q03"]').get_attribute("aria-pressed")=="true"
                page.screenshot(path=str(SHOTS/f"{name}-q03-placeholder.png"),full_page=True)
                page.locator('button[data-code="Q01"]').click()
                assert "Pilot descriptive data available" in page.locator("#sectionDescription").inner_text()
                assert page.locator("#signals tr").count()==2
                assert not errors,errors
                results.append({"viewport":name,"navigation":"PASS","read_only":"PASS",
                                "q03_placeholder":"PASS","synthetic_banner":"PASS",
                                "js_errors":errors})
                page.close()
            browser.close()
        (SHOTS/"results.json").write_text(json.dumps(results,indent=2),encoding="utf-8")
        print("P05.6 browser walkthrough PASS: desktop/mobile navigation, placeholders, counts, no JS exceptions")
    finally:
        server.terminate()
        try:server.wait(timeout=5)
        except subprocess.TimeoutExpired:server.kill()

if __name__=="__main__":run()
