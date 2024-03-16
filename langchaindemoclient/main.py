from langserve import RemoteRunnable
from pprint import pprint
if __name__ == "__main__":
    print("hi")

    chain = RemoteRunnable("http://127.0.0.1:8000/simple/")
    result = chain.invoke({"input": "Flash Gordon"})
    print("Invoke:")
    print(result)

    results = chain.batch([{"input": "Flash Gordon"},{"input": "Snow White"}])
    print("Batch:")
    pprint(results)

    result = chain.stream({"input": "Flash Gordon"})
    print("Stream:")
    for chunk in chain.stream({"input": "Batman"}):
        print(chunk ,end="", flush=True)
