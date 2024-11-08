package ServiceLayer.FileUpload;

import java.time.LocalDateTime;
import java.util.List;

import Utilities.DataClasses.Submission;
import org.springframework.web.multipart.MultipartFile;

public interface IFileUploadService {
    void Activate();
    void Initialize(List<MultipartFile> Files, String Path, Submission submission);
    boolean IsSubmissionOnTime();
}
