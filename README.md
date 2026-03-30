you can access without cloud with helping the given url
https://effective-space-funicular-q7xr7xrg5vvrfvxq-8501.app.github.dev/
working of codespaces (only terminal part)
@kamalkant9928 ➜ /workspaces/my-system (main) $ ls
app.py  dockerfile  requirements.txt
@kamalkant9928 ➜ /workspaces/my-system (main) $ -m my-system-project
bash: -m: command not found
@kamalkant9928 ➜ /workspaces/my-system (main) $ docker build -t student-ml-app .
[+] Building 1.5s (10/10) FINISHED                                                                   docker:default
 => [internal] load build definition from dockerfile                                                           0.0s
 => => transferring dockerfile: 339B                                                                           0.0s
 => [internal] load metadata for docker.io/library/python:3.10-slim                                            1.2s
 => [auth] library/python:pull token for registry-1.docker.io                                                  0.0s
 => [internal] load .dockerignore                                                                              0.1s
 => => transferring context: 2B                                                                                0.1s
 => [1/4] FROM docker.io/library/python:3.10-slim@sha256:4ba18b066cee17f2696cf9a2ba564d7d5eb05a91d6a949326780  0.0s
 => [internal] load build context                                                                              0.1s
 => => transferring context: 13.22kB                                                                           0.0s
 => CACHED [2/4] WORKDIR /app                                                                                  0.0s
 => CACHED [3/4] COPY . .                                                                                      0.0s
 => CACHED [4/4] RUN pip install --no-cache-dir -r requirements.txt                                            0.0s
 => exporting to image                                                                                         0.0s
 => => exporting layers                                                                                        0.0s
 => => writing image sha256:ed9c9cab5add3312e07769772c9bfdeacd0cbe8305a9d8534cd2e93035e1e2ee                   0.0s
 => => naming to docker.io/library/student-ml-app                                                              0.0s
@kamalkant9928 ➜ /workspaces/my-system (main) $ docker run -p 8501:8501 student-ml-app

Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.


  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://172.17.0.2:8501
  External URL: http://13.71.3.97:8501


  port
  
  External URL: http://13.71.3.97:8501

  
