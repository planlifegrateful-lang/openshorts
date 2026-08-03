import os
import saasshorts

# If DEV_STUBS is set, replace heavy pipeline functions with dev stubs
if os.environ.get("DEV_STUBS"):
    try:
        from dev_stubs import generate_full_video as _dev_generate_full_video
        saasshorts.generate_full_video = _dev_generate_full_video
        print("[dev_runner] DEV_STUBS active: saasshorts.generate_full_video patched to dev_stubs")
    except Exception as e:
        print(f"[dev_runner] Failed to patch dev stubs: {e}")

# Run uvicorn programmatically
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
