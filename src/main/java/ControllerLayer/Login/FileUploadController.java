package ControllerLayer.Login;

import ServiceLayer.FileUpload.FileUploadService;
import Utilities.DataClasses.Submission;
import Utilities.LoggerManager.LoggerManager;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.rest.webmvc.support.RepositoryEntityLinks;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.time.LocalDateTime;
import java.util.List;

@RestController
@RequestMapping("/api/submission")
public class FileUploadController {
    private final FileUploadService FileUploader;

    @Autowired
    public FileUploadController(FileUploadService uploader){
        this.FileUploader = uploader;
    }

    @PostMapping("/upload")
    public ResponseEntity<String> UploadSubmission(
            @RequestParam("studentID") String studentID,
            @RequestParam("assignmentTopic") String assignmentTopic,
            @RequestParam("commitContent") String commitContent,
            @RequestParam("commitTime") LocalDateTime commitTime, // 假设前端以字符串形式传递时间
            @RequestParam("files") List<MultipartFile> files,
            @RequestParam("path") String Path){

        Submission submission = new Submission(
                studentID,
                assignmentTopic,
                commitTime,
                null,
                commitContent
        );

        // 这里假设path是用户的学号
        this.FileUploader.Initialize(files, Path, submission);
        LoggerManager.ControllerLogger.info("Files has been sent to backend");
        return ResponseEntity.ok("Files has been sent to backend");
    }
}
