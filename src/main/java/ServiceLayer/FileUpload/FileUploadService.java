package ServiceLayer.FileUpload;

import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.LocalDateTime;
import java.util.Arrays;
import java.util.List;
import java.util.Properties;
import java.util.stream.Collectors;
import java.io.File;

import Utilities.DataClasses.Submission;
import Utilities.Repositories.SubmissionRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import Utilities.LoggerManager.LoggerManager;
import org.springframework.web.multipart.MultipartFile;

@Component
public class FileUploadService implements IFileUploadService {
    private static String UPLOAD_FOLDER;
    private static List<String> ALLOWED_EXTENSIONS;
    private List<MultipartFile> FileList;
    private String SavedPath;
    private Submission submission;
    private LocalDateTime deadline;
    @Autowired
    private SubmissionRepository SubmitRepo;// 自动注入

    static {
        LoadPropertyFile();
    }
    private static void LoadPropertyFile(){
        Properties FileProperty = new Properties();
        try(FileInputStream input = new FileInputStream("properties/file_commitment.properties")){
            FileProperty.load(input);
            UPLOAD_FOLDER = FileProperty.getProperty("upload.folder");
            String Extensions = FileProperty.getProperty("allowed.extensions");
            ALLOWED_EXTENSIONS = Arrays.stream(Extensions.split(",")).map((String::trim)).collect(Collectors.toList());
            LoggerManager.ServiceLogger.info("successfully read file commitment property");
        }
        catch(IOException e){
            LoggerManager.ServiceLogger.error("can not load file commitment property");
        }
    }
    // TODO
    private boolean IsAllowedFile(String FileName){
        // 查找最后一个点的位置
        int dotIndex = FileName.lastIndexOf(".");
        // 如果文件名包含点且点不是第一个字符，截取扩展名并转换为小写
        if (dotIndex > 0 && dotIndex < FileName.length() - 1) {
            String extension = FileName.substring(dotIndex + 1).toLowerCase();
            return ALLOWED_EXTENSIONS.contains(extension);
        }
        return false; // 如果没有扩展名或格式不正确，返回 false
    }
    private void CreateFolder(){
        File folder = new File(this.SavedPath);
        if(!folder.exists()){
            try{
                Files.createDirectories(Paths.get(this.SavedPath));
                LoggerManager.ServiceLogger.info("create folder " + this.SavedPath);
            }
            catch (IOException e){
                LoggerManager.ServiceLogger.error("failed to create dir "+this.SavedPath, e);
            }
        }
    }
    private void SaveFiles(){
        for(MultipartFile file : this.FileList){
            String OriginalFileName = file.getOriginalFilename();
            if(OriginalFileName != null && IsAllowedFile(OriginalFileName)) {
                try {
                    String FileName = Paths.get(OriginalFileName).getFileName().toString();
                    File destination = new File(this.SavedPath, FileName);
                    file.transferTo(destination);
                    LoggerManager.ServiceLogger.info("has saved file : " + file.getName() + " to folder : " + this.SavedPath);
                } catch (IOException e) {
                    LoggerManager.ServiceLogger.error("failed to save file, error is " + e);
                }
            }
            else{
                LoggerManager.ServiceLogger.warn(OriginalFileName+" is invalid or not saved");
            }
        }
    }
    private void SaveToDB(){
        // GetDeadline();
        this.IsSubmissionOnTime();
        SubmitRepo.save(this.submission);
    }
    @Override
    public void Activate(){
        CreateFolder();
        SaveFiles();
        SaveToDB();
    }
    public void GetDeadline(LocalDateTime deadline){
        this.deadline = deadline;
    }
    @Override
    public boolean IsSubmissionOnTime(){
        if(this.submission.getCommitTime().isBefore(this.deadline)){
            LoggerManager.DatabaseLogger.info("commit before deadline");
            submission.setStatus(Submission.Status.Submitted);
            return true;
        }else{
            LoggerManager.DatabaseLogger.info("commit after deadline");
            submission.setStatus(Submission.Status.Late);
            return false;
        }
    }

    @Override
    public void Initialize(List<MultipartFile> Files, String Path, Submission submission){
        this.FileList = Files;
        StringBuilder builder = new StringBuilder();
        builder.append(UPLOAD_FOLDER+"/"+Path);
        this.SavedPath = builder.toString();
        //加入path为2251646,则文件会存储到test/2251646/
        this.submission = submission;
    }
}
