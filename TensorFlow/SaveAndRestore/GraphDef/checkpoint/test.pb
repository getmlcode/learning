
6
zerosConst*
valueB
*    *
dtype0
X
zeroBias
VariableV2*
dtype0*
shared_name *
	container *
shape:

y
zeroBias/AssignAssignzeroBiaszeros*
T0*
use_locking(*
validate_shape(*
_class
loc:@zeroBias
I
zeroBias/readIdentityzeroBias*
T0*
_class
loc:@zeroBias
I
random_uniform/shapeConst*
valueB"   
   *
dtype0
?
random_uniform/minConst*
valueB
 *  ��*
dtype0
?
random_uniform/maxConst*
valueB
 *  �?*
dtype0
r
random_uniform/RandomUniformRandomUniformrandom_uniform/shape*
T0*
dtype0*
seed2 *

seed 
J
random_uniform/subSubrandom_uniform/maxrandom_uniform/min*
T0
T
random_uniform/mulMulrandom_uniform/RandomUniformrandom_uniform/sub*
T0
F
random_uniformAddrandom_uniform/mulrandom_uniform/min*
T0
[
Weights
VariableV2*
dtype0*
shared_name *
	container *
shape
:


Weights/AssignAssignWeightsrandom_uniform*
T0*
use_locking(*
validate_shape(*
_class
loc:@Weights
F
Weights/readIdentityWeights*
T0*
_class
loc:@Weights
6
inputPlaceholder*
dtype0*
shape
:
T
MatMulMatMulinputWeights/read*
T0*
transpose_b( *
transpose_a( 
*
addAddMatMulzeroBias/read*
T0

ReluOUTReluadd*
T0
8

save/ConstConst*
valueB Bmodel*
dtype0
V
save/SaveV2/tensor_namesConst*&
valueBBWeightsBzeroBias*
dtype0
K
save/SaveV2/shape_and_slicesConst*
valueBB B *
dtype0
~
save/SaveV2SaveV2
save/Constsave/SaveV2/tensor_namessave/SaveV2/shape_and_slicesWeightszeroBias*
dtypes
2
e
save/control_dependencyIdentity
save/Const^save/SaveV2*
T0*
_class
loc:@save/Const
h
save/RestoreV2/tensor_namesConst"/device:CPU:0*&
valueBBWeightsBzeroBias*
dtype0
]
save/RestoreV2/shape_and_slicesConst"/device:CPU:0*
valueBB B *
dtype0
�
save/RestoreV2	RestoreV2
save/Constsave/RestoreV2/tensor_namessave/RestoreV2/shape_and_slices"/device:CPU:0*
dtypes
2
|
save/AssignAssignWeightssave/RestoreV2*
T0*
use_locking(*
validate_shape(*
_class
loc:@Weights
�
save/Assign_1AssignzeroBiassave/RestoreV2:1*
T0*
use_locking(*
validate_shape(*
_class
loc:@zeroBias
6
save/restore_allNoOp^save/Assign^save/Assign_1
/
initNoOp^Weights/Assign^zeroBias/Assign"