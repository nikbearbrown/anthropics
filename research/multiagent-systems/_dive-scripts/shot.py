import asyncio, os
from playwright.async_api import async_playwright
SRC="file:///tmp/post.html"
TARGETS=[("claim-newer-models","Newer models recover more of the gap"),
         ("claim-scales","performance scales with model intelligence"),
         ("claim-comparable","the two methods seem comparable in terms of tokens"),
         ("claim-lockout","often successfully lock out other agents"),
         ("quote-collusion","a price war just burns everyone"),
         ("quote-camouflage","report \"typescript\" in its health check"),
         ("hero","Patterns and problems in emerging multiagent systems")]
async def main():
    os.makedirs("pantry/post",exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/opt/pw-browsers/chromium" if os.path.exists("/opt/pw-browsers/chromium") else None)
        pg=await b.new_page(viewport={"width":1600,"height":1000},device_scale_factor=2.4)
        await pg.goto(SRC,wait_until="domcontentloaded",timeout=45000)
        await pg.wait_for_timeout(2500)
        ok=[]
        for name,needle in TARGETS:
            try:
                loc=pg.locator(f"text={needle}").first
                await loc.scroll_into_view_if_needed(timeout=6000)
                await pg.wait_for_timeout(350)
                await loc.evaluate("""e=>{e.style.background='#F6D8DC';e.style.outline='4px solid #C8102E';
                    e.style.padding='22px';e.style.fontFamily='EB Garamond, Georgia, serif';
                    e.style.fontSize='30px';e.style.lineHeight='1.55';e.style.maxWidth='1400px';
                    e.style.margin='40px auto';e.scrollIntoView({block:'center'});}""")
                await pg.wait_for_timeout(250)
                bb = await loc.bounding_box()
                pad = 34
                await pg.screenshot(path=f"pantry/post/{name}.png", clip={
                    "x": max(0, bb["x"]-pad), "y": max(0, bb["y"]-pad),
                    "width": bb["width"]+2*pad, "height": bb["height"]+2*pad})
                ok.append(name)
            except Exception as ex:
                print("MISS",name,str(ex)[:70])
        print("OK:",ok)
        await b.close()
asyncio.run(main())
