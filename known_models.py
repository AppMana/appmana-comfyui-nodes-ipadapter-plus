from comfy.cmd.folder_paths import add_model_folder_path
from comfy.model_downloader import add_known_models, \
    KNOWN_CLIP_VISION_MODELS, KNOWN_LORAS
from comfy.model_downloader_types import HuggingFile

KNOWN_IP_ADAPTER_MODELS = [
    HuggingFile("h94/IP-Adapter", "models/ip-adapter-full-face_sd15.safetensors"),
    HuggingFile("h94/IP-Adapter", "models/ip-adapter-plus-face_sd15.safetensors"),
    HuggingFile("h94/IP-Adapter", "models/ip-adapter-plus_sd15.safetensors"),
    HuggingFile("h94/IP-Adapter", "models/ip-adapter_sd15.safetensors"),
    HuggingFile("h94/IP-Adapter", "models/ip-adapter_sd15_light.safetensors"),
    HuggingFile("h94/IP-Adapter", "models/ip-adapter_sd15_vit-G.safetensors"),
    HuggingFile("h94/IP-Adapter", "sdxl_models/ip-adapter-plus-face_sdxl_vit-h.safetensors"),
    HuggingFile("h94/IP-Adapter", "sdxl_models/ip-adapter-plus_sdxl_vit-h.safetensors"),
    HuggingFile("h94/IP-Adapter", "sdxl_models/ip-adapter_sdxl.safetensors"),
    HuggingFile("h94/IP-Adapter", "sdxl_models/ip-adapter_sdxl_vit-h.safetensors"),
    HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid-plus_sd15.bin"),
    HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid-plusv2_sd15.bin"),
    HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid-plusv2_sdxl.bin"),
    HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid-portrait-v11_sd15.bin"),
    HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid-portrait_sd15.bin"),
    HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid-portrait_sdxl.bin"),
    HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid-portrait_sdxl_unnorm.bin"),
    HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid_sd15.bin"),
    HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid_sdxl.bin"),
    HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter_sd15_light_v11.bin"),
    HuggingFile("ostris/ip-composition-adapter", "ip_plus_composition_sd15.safetensors"),
    HuggingFile("ostris/ip-composition-adapter", "ip_plus_composition_sdxl.safetensors"),
    HuggingFile("Kwai-Kolors/Kolors-IP-Adapter-Plus", "ip_adapter_plus_general.bin", save_with_filename="Kolors-IP-Adapter-Plus.bin"),
]

add_known_models("clip_vision",
                 KNOWN_CLIP_VISION_MODELS,
                 HuggingFile("h94/IP-Adapter", "models/image_encoder/model.safetensors",
                             save_with_filename="laion_CLIP-ViT-bigG-14-laion2B-39B-b160k.safetensors"),
                 HuggingFile("h94/IP-Adapter", "sdxl_models/image_encoder/model.safetensors",
                             save_with_filename="laion_CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors"),
                 HuggingFile("Kwai-Kolors/Kolors-IP-Adapter-Plus", "image_encoder/pytorch_model.bin",
                             save_with_filename="clip-vit-large-patch14-336.bin"),
                 )

add_known_models("loras",
                 KNOWN_LORAS,
                 HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid-plus_sd15_lora.safetensors"),
                 HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid-plusv2_sd15_lora.safetensors"),
                 HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid-plusv2_sdxl_lora.safetensors"),
                 HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid_sd15_lora.safetensors"),
                 HuggingFile("h94/IP-Adapter-FaceID", "ip-adapter-faceid_sdxl_lora.safetensors"),
                 )

FOLDER_NAME = "ipadapter"

add_model_folder_path(FOLDER_NAME)
add_model_folder_path("insightface")
