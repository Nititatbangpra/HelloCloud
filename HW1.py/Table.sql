SELECT Students.student_id , Students.f_name ,Students.l_name 
, Subjects.sub_id , Subjects.subject_name
,Registration.grade , Teachers.f_name , Teachers.l_name from Students
JOIN Registration
    on Students.student_id = Registration.student_id
JOIN Subjects
    on Registration.sub_id = Subjects.sub_id
JOIN Teachers
    on Subjects.teacher_id = Teachers.teacher_id
;