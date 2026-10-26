"""Small utility nodes for workflow plumbing."""

class _Noop:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": ("STRING", {"default": ""})}}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "run"
    CATEGORY = "utils/text"

    def run(self, value):
        return (value,)


NODE_CLASS_MAPPINGS = {"UtilPassThrough": _Noop}
NODE_DISPLAY_NAME_MAPPINGS = {"UtilPassThrough": "Util Pass Through"}
