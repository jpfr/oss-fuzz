# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Implementation of a filestore using Github actions artifacts."""
import logging
import os
import shutil
import tarfile
import tempfile

import http_utils
import filestore
from filestore.github_actions import github_api
from third_party.github_actions_toolkit.artifact import artifact_client


def tar_directory(directory, archive_path):
  """Tars a |directory| and stores archive at |archive_path|. |archive_path|
  must end in .tar"""
  assert archive_path.endswith('.tar')
  # Do this because make_archive will append the extension to archive_path.
  archive_path = os.path.splitext(archive_path)[0]

  root_directory = os.path.abspath(directory)
  shutil.make_archive(archive_path,
                      'tar',
                      root_dir=root_directory,
                      base_dir='./')


class GithubActionsFilestore(filestore.BaseFilestore):
  """Implementation of BaseFilestore using Github actions artifacts. Relies on
  github_actions_toolkit for using the GitHub actions API and the github_api
  module for using GitHub's standard API. We need to use both because the GitHub
  actions API is the only way to upload an artifact but it does not support
  downloading artifacts from other runs. The standard GitHub API does support
  this however."""

  def __init__(self, config):
    super().__init__(config)
    self.github_api_http_headers = github_api.get_http_auth_headers(config)

  def upload_directory(self, name, directory):  # pylint: disable=no-self-use
    """Uploads |directory| as artifact with |name|."""
    with tempfile.TemporaryDirectory() as temp_dir:
      archive_path = os.path.join(temp_dir, name + '.tar')
      tar_directory(directory, archive_path)
      file_paths = [archive_path]

      return artifact_client.upload_artifact(name, file_paths, temp_dir)

  def download_corpus(self, name, dst_directory):  # pylint: disable=unused-argument,no-self-use
    """Downloads the corpus located at |name| to |dst_directory|."""
    return self._download_artifact(name, dst_directory)

  def _find_artifact(self, name):
    """Finds an artifact using the GitHub API and returns it."""
    logging.debug('listing artifact')
    artifacts = self._list_artifacts()
    artifact = github_api.find_artifact(name, artifacts)
    logging.debug('Artifact: %s.', artifact)
    return artifact

  def _download_artifact(self, name, dst_directory):
    """Downloads artifact with |name| to |dst_directory|."""
    artifact = self._find_artifact(name)
    if not artifact:
      logging.warning('Could not download artifact: %s.', name)
      return artifact
    download_url = artifact['archive_download_url']
    with tempfile.TemporaryDirectory() as temp_dir:
      if not http_utils.download_and_unpack_zip(
          download_url, temp_dir, headers=self.github_api_http_headers):
        return False

      artifact_tarfile_path = os.path.join(temp_dir, name + '.tar')
      if not os.path.exists(artifact_tarfile_path):
        logging.error('Artifact zip did not contain a tarfile.')
        return False

      # TODO(jonathanmetzman): Replace this with archive.unpack from
      # libClusterFuzz so we can avoid path traversal issues.
      with tarfile.TarFile(artifact_tarfile_path) as artifact_tarfile:
        artifact_tarfile.extractall(dst_directory)
    return True

  def _list_artifacts(self):
    """Returns a list of artifacts."""
    return github_api.list_artifacts(self.config.project_repo_owner,
                                     self.config.project_repo_name,
                                     self.github_api_http_headers)

  def download_latest_build(self, name, dst_directory):
    """Downloads latest build with name |name| to |dst_directory|."""
    return self._download_artifact(name, dst_directory)

  def download_coverage(self, name, dst_directory):
    """Downloads the latest project coverage report."""
    return self._download_artifact(name, dst_directory)
