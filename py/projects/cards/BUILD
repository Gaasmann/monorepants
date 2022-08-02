resource(name="pyproject", source="pyproject.toml")

python_awslambda(
  name="lambda",
  runtime="python3.9",
  handler="turbocorp.cards.entrypoint:handler",
  dependencies=[
      "py/projects/cards/ext-config/something:tutu",
      "py/projects/cards/ext-config/something:protobuf",
      "py/projects/cards/ext-config/something:aresource"
  ]
)
