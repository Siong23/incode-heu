#!/usr/bin/python3.7.3

import subprocess

def get_pod_info(namespace,label_selector):
   try:
      command1 = f"kubectl get pods -n {namespace} --selector={label_selector} -o jsonpath='{{.items[0].metadata.name}}'"
      command2 = f"kubectl get pods -n {namespace} --selector={label_selector} -o jsonpath='{{.items[0].spec.nodeName}}'"
      pod_name = subprocess.check_output([command1], shell=True).decode('utf-8')
      node_name = subprocess.check_output([command2], shell=True).decode('utf-8') 
      return {"name": pod_name, "node_name": node_name}

   except subprocess.CalledProcessError as e:
      print(f"Error: Unable to get pod name. {e}")
      return None

namespace = "liqo-demo"
label_selector = "app=myapp"
pod_info = get_pod_info(namespace,label_selector)

if pod_info:
   print(f"Pod Name: {pod_info['name']}, Node Name: {pod_info['node_name']}")
else:
   print("Unable to retrieve pod name.")

subprocess.run(["kubectl", "cordon", pod_info['node_name']])
subprocess.run(["kubectl", "scale", "--replicas=2", "deployments/myapp-deployment", "-n", "liqo-demo"])
subprocess.run(["kubectl", "delete", "pod", pod_info['name'], "-n", "liqo-demo"])
subprocess.run(["kubectl", "scale", "--replicas=1", "deployments/myapp-deployment", "-n", "liqo-demo"])
subprocess.run(["kubectl", "uncordon", pod_info['node_name']])
