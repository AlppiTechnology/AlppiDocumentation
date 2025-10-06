---
status: new
icon: material/routes
---


#Route Permissions


## Campus
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar |campus/list/ | {{ superuser() }} |
| Visualizar |campus/[int:pk]/ | {{ superuser() }} |
| Criar |campus/create/ | {{ superuser() }} |
| Atualizar |campus/[int:pk]/update/ | {{ superuser() }} |
| Deletar |campus/[int:pk]/delete/ | {{ superuser() }} |
| Mudar Status |campus/[int:pk]/changestatus/ | {{ superuser() }} |


## Campus Settings
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Visualizar | campussettings/[int:pk_campus]/ | {{ superuser() }} {{ admin() }}  |
| Atualizar | campussettings/[int:pk_campus]/ | {{ superuser() }} {{ admin() }}  |
| Mudar Senha | campussettings/change-password/  | {{ superuser() }} {{ admin() }}  |


## Employee
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | employee/list/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} |
| Visualizar | employee/[int:pk]/ | {{ superuser() }} {{ admin() }} |
| Criar | employee/create/ | {{ superuser() }} {{ admin() }} |
| Atualizar | employee/[int:pk]/update/ | {{ superuser() }} {{ admin() }} |
| Deletar | employee/[int:pk]/delete/ | {{ superuser() }} |
| Mudar Status | employee/[int:pk]/changestatus/ | {{ superuser() }} {{ admin() }}|
| Criar por Arquivo | employee/uploadfile/ | {{ superuser() }} {{ admin() }}|
| Baixar Template | employee/gettemlpate/ | {{ superuser() }} {{ admin() }}|
| Mudar Senha | employee/change-password/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }} |

## Student
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | student/list/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} |
| Visualizar | student/[int:pk]/ | {{ superuser() }} {{ admin() }} |
| Criar | student/create/ | {{ superuser() }} {{ admin() }} |
| Atualizar | student/[int:pk]/update/ | {{ superuser() }} {{ admin() }} |
| Deletar | student/[int:pk]/delete/ | {{ superuser() }} |
| Mudar Status | student/[int:pk]/changestatus/ | {{ superuser() }} {{ admin() }} |
| Criar por Arquivo | student/uploadfile/ | {{ superuser() }} {{ admin() }}|
| Baixar Template | student/gettemlpate/ | {{ superuser() }} {{ admin() }}|
| Mudar Senha | student/change-password/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }} {{ student() }} |

## City
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | city/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }} {{ student() }}|

## User Groups
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | groups/ | {{ superuser() }} {{ admin() }} |
| Criar | groups/create/ | {{ superuser() }}|


## Skill Settings
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | skillsettings/list/ | {{ superuser() }} {{ admin() }} |
| Visualizar | skillsettings/[int:pk]/ | {{ superuser() }} {{ admin() }} |
| Criar | skillsettings/create/ | {{ superuser() }} {{ admin() }} |
| Atualizar | skillsettings/[int:pk]/update/ | {{ superuser() }} {{ admin() }} |
| Deletar | skillsettings/[int:pk]/delete/ | {{ superuser() }} |
| Mudar Status | skillsettings/[int:pk]/changestatus/ | {{ superuser() }} {{ admin() }} |

## School Year
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar Resumido | schoolyear/list/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} |
| Listar Completo | schoolyear/listinfo/ | {{ superuser() }} {{ admin() }} |
| Visualizar | schoolyear/[int:pk]/ | {{ superuser() }} {{ admin() }} |
| Criar | schoolyear/create/ | {{ superuser() }} {{ admin() }} |
| Atualizar | schoolyear/[int:pk]/update/ | {{ superuser() }} {{ admin() }} |
| Deletar | schoolyear/[int:pk]/delete/ | {{ superuser() }} |
| Mudar Status | schoolyear/[int:pk]/changestatus/ | {{ superuser() }} {{ admin() }} |

## Subject Area
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | subjectarea/list/ | {{ superuser() }} {{ admin() }} |
| Visualizar | subjectarea/[int:pk]/ | {{ superuser() }} {{ admin() }} |
| Criar | subjectarea/create/ | {{ superuser() }} {{ admin() }} |
| Atualizar | subjectarea/[int:pk]/update/ | {{ superuser() }} {{ admin() }} |
| Deletar | subjectarea/[int:pk]/delete/ | {{ superuser() }} |
| Mudar Status | subjectarea/[int:pk]/changestatus/ | {{ superuser() }} {{ admin() }} |


## Subject
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | subject/list/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} |
| Visualizar | subject/[int:pk]/ | {{ superuser() }} {{ admin() }} |
| Criar | subject/create/ | {{ superuser() }} {{ admin() }} |
| Atualizar | subject/[int:pk]/update/ | {{ superuser() }} {{ admin() }} |
| Deletar | subject/[int:pk]/delete/ | {{ superuser() }} |
| Mudar Status | subject/[int:pk]/changestatus/ | {{ superuser() }} {{ admin() }} |


## Shift
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | shift/list/ | {{ superuser() }} {{ admin() }} |


## School Level
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | schoollevel/list/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} |
| Criar | schoollevel/create/ | {{ superuser() }} {{ admin() }} |
| Atualizar | schoollevel/[int:pk]/update/ | {{ superuser() }} {{ admin() }} |
| Deletar | schoollevel/[int:pk]/delete/ | {{ superuser() }} |
| Mudar Status | schoollevel/[int:pk]/changestatus/ | {{ superuser() }} {{ admin() }} |

## School Grade
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | schoolgrade/list/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} |
| Criar | schoolgrade/create/ | {{ superuser() }} {{ admin() }} |
| Atualizar | schoolgrade/[int:pk]/update/ | {{ superuser() }} {{ admin() }} |
| Deletar | schoolgrade/[int:pk]/delete/ | {{ superuser() }} |
| Mudar Status | schoolgrade/[int:pk]/changestatus/ | {{ superuser() }} {{ admin() }} |

## Term Type
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | termtype/list/ | {{ superuser() }} {{ admin() }} |
| Criar | termtype/create/ | {{ superuser() }} {{ admin() }} |
| Atualizar | termtype/[int:pk]/update/ | {{ superuser() }} {{ admin() }} |
| Deletar | termtype/[int:pk]/delete/ | {{ superuser() }} |
| Mudar Status | termtype/[int:pk]/changestatus/ | {{ superuser() }} {{ admin() }} |

## Term
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | term/list/ | {{ superuser() }} {{ admin() }} |
| Criar | term/create/ | {{ superuser() }} {{ admin() }} |
| Atualizar | term/[int:pk]/update/ | {{ superuser() }} {{ admin() }} |
| Deletar | term/[int:pk]/delete/ | {{ superuser() }} |
| Mudar Status | term/[int:pk]/changestatus/ | {{ superuser() }} {{ admin() }} |

## Class
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | class/list/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} |
| Visualizar | class/[int:pk]/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }}  |
| Criar | class/create/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} |
| Atualizar | class/[int:pk]/update/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} |
| Deletar | class/[int:pk]/delete/ | {{ superuser() }} |
| Mudar Status | class/[int:pk]/changestatus/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} |

## Pedagogical
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | pedagogical/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }} |

## Subject Grade
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | subjectgrade/[int:class_id]/[int:pedagogical_id]/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }}  |
| Atualizar | subjectgrade/[int:class_id]/[int:pedagogical_id]/[int:term_id]/update/ |{{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }}  |

## Skill Grade
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | skillgrade/[int:class_id]/[int:pedagogical_id]/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }}  |
| Atualizar | skillgrade/[int:class_id]/[int:pedagogical_id]/[int:term_id]/[int:skill_id]/update/ |{{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }}  |

## Student Presence
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | studentpresence/[int:class_id]/[int:pedagogical_id]/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }}  |
| Atualizar | studentpresence/[int:class_id]/[int:pedagogical_id]/update/ |{{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }}  |




## Internal Note
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | internal_note/list/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }} {{ student() }} |
| Visualizar | internal_note/[int:pk]/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }} {{ student() }} |
| Criar | internal_note/create/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} |
| Atualizar | internal_note/[int:pk]/update/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} |
| Atualiza Parcialmente | internal_note/[int:pk]/partial_update/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }} {{ student() }} |
| Deletar | internal_note/[int:pk]/delete/ | {{ superuser() }} |

## Internal Note Comment
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Criar | internal_note/[int:pk_internal_note]/comment/create/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }} {{ student() }} |
| Atualizar | internal_note/[int:pk_internal_note]/comment/[int:pk_internal_note_comment]/update/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }} {{ student() }} |
| Deletar | internal_note/[int:pk_internal_note]/comment/[int:pk_internal_note_comment]/delete/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} {{ teacher() }} {{ student() }} |

## Internal Note Settings
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Atualizar | internal_note_settings/update/ |{{ superuser() }} {{ admin() }} |

## Disciplinary Grade
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | disciplinary_grade/list/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} |
| Atualizar | disciplinary_grade/[int:pk_disciplinary_grade]/update/ |{{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }}   |

## regulaments
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | regulaments/list/ | {{ superuser() }} {{ admin() }} {{ coordinator() }} {{ evaluator() }} |

## Flow Disciplinary Grade
| Ação | Rota | Permissões |
| :-------------- | ------------- | --- |
| Listar | flow_disciplinary_grade/list/ | {{ superuser() }} |
