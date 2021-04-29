from typing import Iterable
from typing import Union

from faker.providers.file import Provider as FileProvider
from hypothesis.strategies import SearchStrategy
from hypothesis.strategies import one_of
from hypothesis.strategies import sampled_from


_APPLICATION_MIME_TYPES = list(FileProvider.application_mime_types)
_AUDIO_MIME_TYPES = list(FileProvider.audio_mime_types)
_IMAGE_MIME_TYPES = list(FileProvider.image_mime_types)
_MESSAGE_MIME_TYPES = list(FileProvider.message_mime_types)
_MODEL_MIME_TYPES = list(FileProvider.model_mime_types)
_MULTIPART_MIME_TYPES = list(FileProvider.multipart_mime_types)
_TEXT_MIME_TYPES = list(FileProvider.text_mime_types)
_VIDEO_MIME_TYPES = list(FileProvider.video_mime_types)
_MIME_TYPES = {
    "application": sampled_from(_APPLICATION_MIME_TYPES),
    "audio": sampled_from(_AUDIO_MIME_TYPES),
    "image": sampled_from(_IMAGE_MIME_TYPES),
    "message": sampled_from(_MESSAGE_MIME_TYPES),
    "model": sampled_from(_MODEL_MIME_TYPES),
    "multipart": sampled_from(_MULTIPART_MIME_TYPES),
    "text": sampled_from(_TEXT_MIME_TYPES),
    "video": sampled_from(_VIDEO_MIME_TYPES),
}


def mime_types(
    category: Union[str, Iterable[str], None] = None
) -> SearchStrategy[str]:
    if category is None:
        return one_of(*_MIME_TYPES.values())
    elif isinstance(category, str):
        return _MIME_TYPES[category]
    else:
        return one_of(*(v for k, v in _MIME_TYPES.items() if k in category))
