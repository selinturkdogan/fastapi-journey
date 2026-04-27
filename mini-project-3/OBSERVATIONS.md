1. What is the difference between a Pod and a Deployment? Why would you use a Deployment instead of a bare Pod?

A Pod is just a single running container. A Deployment manages it automatically — if it crashes, Deployment brings it back. That's why I used Deployment instead of a bare Pod.

2. Why is ConfigMap used for the MongoDB URL instead of hardcoding it?

If I hardcode the URL and it changes later, I have to update every file. With ConfigMap I just change one place. Much easier.

3. What happened to the original Pod when you scaled to 3 replicas?

It stayed. Two new Pods were created next to it. I could tell because the original one had a much older AGE when I ran kubectl get pods.

4. What would happen if the MongoDB Pod crashed?

The app would lose its database and stop working for a bit. But Kubernetes would restart the Pod automatically so it recovers on its own.

5. What surprised you?

Docker Desktop wouldn't start at all so I had to use the hyperv driver instead, I didn't even know that was an option. Also kubectl version --short gave an error, apparently that flag was removed. I just used kubectl version and it worked fine.
