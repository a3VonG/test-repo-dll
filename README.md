# test-repo-dll
A test repo to mock the use case of the dll.
The requirement is to make a .dll which exposes the `cudaIsAvailable` and `pipelineTest` calls.
The packages that need to be included are found in the `requirements.txt` file (`pip install requirements.txt` in your virtualenv) it should also work with the `requirements_cuda.txt` file. ()

Some rules:
- You cannot manually rewrite the code in C/C++ as in the real project this would be unfeasible due to the size of the code project.
-  
 




