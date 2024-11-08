package Utilities.DataClasses;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name="submission")
public class Submission {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "studentID", length = 7, nullable = false)
    private String studentID;

    @Column(name = "assignmentTopic", length = 100, nullable = false)
    private String assignmentTopic;

    @Column(name = "commitTime", nullable = false)
    private LocalDateTime commitTime;

    @Enumerated(EnumType.STRING)
    @Column(name = "status", nullable = false)
    private Status status;

    @Column(name = "commitContent", columnDefinition = "TEXT")
    private String commitContent;

    public Submission(String studentID, String assignmentTopic, LocalDateTime commitTime, Status status, String commitContent) {
        this.studentID = studentID;
        this.assignmentTopic = assignmentTopic;
        this.commitTime = commitTime;
        this.status = status;
        this.commitContent = commitContent;
    }

    // Getters 和 Setters
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getStudentID() {
        return studentID;
    }

    public void setStudentID(String studentID) {
        this.studentID = studentID;
    }

    public String getAssignmentTopic() {
        return assignmentTopic;
    }

    public void setAssignmentTopic(String assignmentTopic) {
        this.assignmentTopic = assignmentTopic;
    }

    public LocalDateTime getCommitTime() {
        return commitTime;
    }

    public void setCommitTime(LocalDateTime commitTime) {
        this.commitTime = commitTime;
    }

    public Status getStatus() {
        return status;
    }

    public void setStatus(Status status) {
        this.status = status;
    }

    public String getCommitContent() {
        return commitContent;
    }

    public void setCommitContent(String commitContent) {
        this.commitContent = commitContent;
    }

    // 枚举类 Status，定义提交状态
    public enum Status {
        Submitted,
        Graded,
        Late
    }
}
