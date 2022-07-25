from collections import namedtuple

#DEFINING THE OUTPUTS OF THE DIFFERENT COMPONENTS

DataIngestionArtifact = namedtuple("DataIngestionArtifact",
[ "train_file_path", "test_file_path", "is_ingested", "message"])
