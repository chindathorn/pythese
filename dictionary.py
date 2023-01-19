stack_dict = {
  "frontend": "Javascript",
  "backend": "Node JS",
  "markup": "HTML and JSX",
}

stack_dict["styling"] = "CSS"

stack_dict["markup"] = "HTML only"

stack_dict.update({"framework": "React/Next"})

if "Tailwind CSS" not in stack_dict.keys():
    stack_dict["CSS Framework"] = "Tailwind CSS"

try:
    stack_dict["Deployment"] = "Kubernet"
    stack_dict["markup"] = "HTML and XML"
except:
    print("Already exist")

print(stack_dict)
