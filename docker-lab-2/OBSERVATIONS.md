# OBSERVATIONS — Docker Lab 2

## 1. docker run vs kubectl run
With docker run the container ran directly on my computer and that was it.
With kubectl run it felt different, Kubernetes scheduled the pod, assigned
it an IP and a node, and started tracking it. Same image but a lot more
happened in the background this time.

## 2. Scheduler in kubectl describe
The first event I saw was Scheduled from default-scheduler. It assigned
the pod to the minikube node. This is the kube-scheduler, it decides
which node a pod runs on.

## 3. kube-system components
- **etcd-minikube**: Keeps all the cluster data. Everything about the
  cluster state is stored here.
- **kube-apiserver-minikube**: All my kubectl commands went through here.
  It is like the front door of the cluster.

## 4. Python observation
When I ran platform.node() inside the pod it printed my-pod not my
laptop name. The pod has its own hostname set to its name. The container
does not know it is running on my machine, it is completely isolated.

## 5. Task 6 reflection
I deleted the pod and it did not come back. There was nothing watching
over it to restart it. If I used a Deployment it would have come back
automatically because a ReplicaSet would be monitoring it. A standalone
pod has no controller so it just stays deleted.