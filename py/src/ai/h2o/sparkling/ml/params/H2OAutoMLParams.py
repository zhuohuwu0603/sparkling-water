#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from ai.h2o.sparkling.ml.params.H2OAutoMLBuildControlParams import H2OAutoMLBuildControlParams
from ai.h2o.sparkling.ml.params.H2OAutoMLBuildModelsParams import H2OAutoMLBuildModelsParams
from ai.h2o.sparkling.ml.params.H2OAutoMLInputParams import H2OAutoMLInputParams
from ai.h2o.sparkling.ml.params.H2OAutoMLStoppingCriteriaParams import H2OAutoMLStoppingCriteriaParams
from ai.h2o.sparkling.ml.params.H2OCommonParams import H2OCommonParams
from ai.h2o.sparkling.ml.params.HasMonotoneConstraints import HasMonotoneConstraints
from ai.h2o.sparkling.ml.params.HasPreProcessing import HasPreProcessing
from pyspark.ml.param import *


class H2OAutoMLParams(
    H2OCommonParams,
    H2OAutoMLBuildControlParams,
    H2OAutoMLBuildModelsParams,
    H2OAutoMLInputParams,
    H2OAutoMLStoppingCriteriaParams,
    HasMonotoneConstraints,
    HasPreProcessing
):
    pass
