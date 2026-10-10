from fastapi import FastAPI
import asyncio

app = FastAPI()

"""
--- BACKGROUND TASKS EXPLANATION ---

CLAIM 5: 
When using `BackgroundTasks`, the execution occurs after the HTTP response has already been sent to the client. If the scheduled background task is a standard synchronous `def`, FastAPI executes it in an external threadpool. However, if the scheduled task is defined with `async def`, it is awaited directly on the main event loop.

CLAIM 6: 
It is important to note that `BackgroundTasks` are kept strictly in the process memory. They do not survive a process exit or a server crash. Therefore, they are not a durable or distributed task queue (like Celery), and should not be used for critical jobs that must survive a restart.
"""


"""
--- SYNCHRONOUS DECLARATION ---

CLAIM 1: 
A path operation declared with a standard `def` is executed by FastAPI outside of the main event loop. Instead, it is offloaded to a worker threadpool. This design ensures that executing heavy or blocking synchronous code does not freeze the server for other clients.
"""
@app.get("/sync-route")
def sync_route():
    return {"status": "synchronous execution"}


"""
--- ASYNCHRONOUS DECLARATION ---

CLAIM 2: 
A path operation declared with `async def` runs directly on the application's main event loop as a coroutine.

CLAIM 3: 
Because it runs on the event loop, using a blocking call like `time.sleep()` inside an `async def` function is a critical flaw. The `async def` declaration does not magically make the code non-blocking; `time.sleep()` will hold the entire event loop, freezing the server and forcing all other concurrent requests to wait until the sleep finishes.

CLAIM 4: 
To properly introduce a delay inside an asynchronous operation without blocking the server, one must use `await asyncio.sleep(...)`. This properly suspends the current coroutine, yielding control back to the event loop so it can handle other work in the meantime. It is not interchangeable with `time.sleep()`.
"""
@app.get("/async-route")
async def async_route():
    return {"status": "asynchronous execution"}