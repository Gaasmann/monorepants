from pathlib import Path

from pants.engine.fs import DigestContents, Digest, FileContent, CreateDigest, Snapshot
from pants.engine.internals.selectors import Get
from pants.engine.rules import collect_rules, rule
from pants.engine.target import (
    SingleSourceField,
    Target,
    COMMON_TARGET_FIELDS,
    Dependencies,
    GenerateSourcesRequest,
    GeneratedSources,
    TargetFilesGenerator,
    MultipleSourcesField,
    OverridesField,
)
from pants.engine.unions import UnionRule
import logging

logger = logging.getLogger(__name__)


class YamlSourceField(SingleSourceField):
    expected_file_extensions = (".yaml",)


class TutuDependenciesField(Dependencies):
    pass


class GenerateTutuRequest(GenerateSourcesRequest):
    input = YamlSourceField
    output = YamlSourceField


class TutuSourceTarget(Target):
    alias = "tutu_source"
    core_fields = (*COMMON_TARGET_FIELDS, TutuDependenciesField, YamlSourceField)


class TutuGeneratorSourcesField(MultipleSourcesField):
    default = (".yaml",)
    expected_file_extensions = (".yaml",)


class TutuSourcesOverridesField(OverridesField):
    pass


class TutuSourcesGeneratorTarget(TargetFilesGenerator):
    alias = "tutu_sources"
    generated_target_cls = TutuSourceTarget
    core_fields = (
        *COMMON_TARGET_FIELDS,
        TutuGeneratorSourcesField,
        TutuSourcesOverridesField,
    )
    copied_fields = COMMON_TARGET_FIELDS
    moved_fields = (TutuDependenciesField,)


@rule
async def generate_tutu(request: GenerateTutuRequest) -> GeneratedSources:
    source_snapshot = request.protocol_sources
    digest_contents = await Get(DigestContents, Digest, source_snapshot.digest)
    result_file_content: list[FileContent] = []
    for file_content in digest_contents:
        raw_txt = file_content.content.decode()
        new_content = raw_txt.replace("value", "tutu!")
        result_path = (
            Path(file_content.path).parent / "generated" / Path(file_content.path).name
        )
        result_file_content.append(FileContent(str(result_path), new_content.encode()))
    result_digest = await Get(Digest, CreateDigest(result_file_content))
    result_snapshot = await Get(Snapshot, Digest, result_digest)
    logger.info(result_snapshot)
    return GeneratedSources(result_snapshot)


def rules():
    return [
        *collect_rules(),
        UnionRule(GenerateSourcesRequest, GenerateTutuRequest),
    ]


def target_types():
    return [TutuSourceTarget, TutuSourcesGeneratorTarget]
