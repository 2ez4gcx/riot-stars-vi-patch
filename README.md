# Riot Stars — bản dịch tiếng Việt

Bản vá (patch) Việt hoá cho trò chơi PlayStation 1 *Riot Stars* (Hect, 1997,
mã đĩa **SLPS-00829**, bản Nhật).

Đây là dự án của người hâm mộ, không liên quan tới Hect. Gói này **không
chứa** đĩa gốc hay bất kỳ dữ liệu nào của trò chơi. Bạn cần có ảnh đĩa gốc của
chính mình; bản vá chỉ ghi phần chữ tiếng Việt, phông chữ và vài byte mã điều
chỉnh lên ảnh đĩa đó.

## Tóm tắt 5 bước

1. Tải file vá `riot-stars-vi.rsvi` và `apply_patch.py` (mục 0).
2. Kiểm đĩa gốc Nhật của bạn có SHA-256 bắt đầu bằng `18a138b6` (mục 1–2).
3. Chạy `apply_patch.py` với đĩa gốc (mục 3). Đĩa gốc không bị sửa.
4. Kiểm SHA-256 đĩa ra bắt đầu bằng `ec6b6862` (mục 4).
5. Mở `Riot Stars (VN).cue` bằng giả lập (mục 6).

Các file trong gói:

| File | Dùng để |
|---|---|
| `riot-stars-vi.rsvi` | Bản vá tiếng Việt (khoảng 417 KB) |
| `apply_patch.py` | Trình áp vá bằng Python, tự kiểm SHA-256 trước và sau, tự tạo `.cue` (mục 3) |
| `tao_cue.bat` | Tạo file `.cue` đúng tên cho file `.bin` (kéo thả hoặc nháy đúp, mục 4) |
| `README.md` | Hướng dẫn này |

---

## Hình ảnh

| | |
|---|---|
| ![Menu](docs/anh/01-menu.png) | ![Nhập tên](docs/anh/02-nhap-ten.png) |
| Menu đầu game | Màn nhập tên, bảng chữ Latin |
| ![Xác nhận tên](docs/anh/03-xac-nhan-ten.png) | ![Thoại trận đầu](docs/anh/04-thoai-tran-dau.png) |
| Hộp xác nhận tên | Thoại trong trận đầu |
| ![Hai khung thoại](docs/anh/05-thoai-hai-khung.png) | ![Giao quân](docs/anh/06-giao-quan.png) |
| Hai khung thoại cùng lúc | Tên nhân vật chính chèn vào lời thoại |

Ảnh chụp trên DuckStation với OpenBIOS.

## 0. Tải file về

- **Tải cả gói (dễ nhất):** trên trang repo, bấm nút xanh **Code** →
  **Download ZIP**, rồi giải nén. Bạn có đủ `riot-stars-vi.rsvi`,
  `apply_patch.py` và `tao_cue.bat`.
- **Tải riêng từng file:** bấm vào tên file trong danh sách (ví dụ
  `riot-stars-vi.rsvi`), rồi bấm nút **tải xuống** (mũi tên ⤓ ở góc phải,
  cạnh nút *Raw*). Đừng dùng chuột phải → "Lưu liên kết": cách đó tải về trang
  web chứ không phải file vá.

Kiểm kích thước sau khi tải: file `.rsvi` phải khoảng **410–420 KB**. Nếu chỉ vài
KB hoặc mở ra thấy chữ HTML thì bạn đã tải nhầm trang web, tải lại.

## 1. Chuẩn bị ảnh đĩa gốc

Bạn cần ảnh đĩa dạng **`.bin` + `.cue`** (Mode 2, 2352 byte mỗi sector) của
đĩa Nhật SLPS-00829. Đây là định dạng mà các phần mềm đọc đĩa PS1 phổ biến
(ImgBurn, CDRDAO, Alcohol 120%…) xuất ra khi chọn kiểu "BIN/CUE". Một số lưu ý:

- Ảnh đĩa phải có **đúng một file `.bin`**. Nếu `.cue` của bạn liệt kê nhiều
  file (Track 01, Track 02…), đó là kiểu chia track, không dùng trực tiếp được.
- File `.iso` (2048 byte mỗi sector) **không** dùng được: bản vá tính theo
  sector 2352 byte có mã sửa lỗi.
- Kích thước đúng của `.bin`: **151.713.408 byte** (64.504 sector).

Bản vá được tạo từ đúng một ảnh đĩa; ảnh khác dù "cùng game" cũng có thể lệch
vài byte. Vì vậy phải kiểm SHA-256 trước khi áp.

## 2. Kiểm SHA-256 của ảnh đĩa gốc

SHA-256 là "dấu vân tay" của file: hai file giống nhau từng byte thì ra cùng
một chuỗi 64 ký tự. Ảnh đĩa gốc phải cho ra đúng:

```
18a138b66ee070ce96a0c6aa559176a4631780e5c52d415289aaef99e2b8479f
```

Cách tính trên từng hệ điều hành (thay `TEN_FILE.bin` bằng tên file của bạn;
nếu đường dẫn có khoảng trắng thì đặt trong dấu ngoặc kép):

**Windows, dùng Command Prompt (cmd):**

```
certutil -hashfile "TEN_FILE.bin" SHA256
```

Mở cmd bằng cách gõ `cmd` vào ô tìm kiếm của Start; dùng lệnh `cd` để vào thư
mục chứa file, hoặc kéo thả file vào cửa sổ cmd để dán đường dẫn. Kết quả hiện
ở dòng thứ hai, có thể có khoảng trắng giữa các cặp ký tự, cứ bỏ khoảng trắng
mà so.

**Windows, dùng PowerShell:**

```
Get-FileHash "TEN_FILE.bin" -Algorithm SHA256
```

Cột `Hash` là kết quả (chữ in hoa, so không phân biệt hoa thường).

**macOS (Terminal):**

```
shasum -a 256 "TEN_FILE.bin"
```

**Linux:**

```
sha256sum "TEN_FILE.bin"
```

File 145 MB nên tính mất vài giây. Chỉ cần so **8 ký tự đầu** là đủ để nhận
ra: đĩa gốc đúng bắt đầu bằng `18a138b6`. Nếu khác, xem mục 5.

`apply_patch.py` cũng tự kiểm SHA-256 này; đĩa sai thì nó dừng và không ghi gì.

## 3. Áp vá bằng Python (Windows, macOS, Linux)

Cần Python 3 (tải từ python.org; trên Windows khi cài nhớ tick "Add Python to
PATH"). Cách này **không sửa** file gốc mà tạo file mới, tự kiểm SHA-256 và tự
tạo luôn file `.cue`.

1. Đặt `apply_patch.py`, `riot-stars-vi.rsvi` và file `.bin` gốc vào cùng một
   thư mục.
2. Mở cửa sổ lệnh tại thư mục đó. Windows: mở thư mục trong File Explorer, bấm
   vào thanh địa chỉ, gõ `cmd` rồi Enter. macOS/Linux: mở Terminal tại thư mục.
3. Chạy lệnh (thay `TEN_FILE_GOC.bin` bằng tên file gốc của bạn, giữ nguyên dấu
   ngoặc kép):

```
python apply_patch.py "TEN_FILE_GOC.bin"
```

Trên macOS/Linux nếu báo không có `python` thì dùng `python3`.

Lệnh tạo **`Riot Stars (VN).bin`** và **`Riot Stars (VN).cue`** ngay cạnh file
gốc. Muốn đặt tên khác thì ghi thêm tên file vá và tên đĩa ra:

```
python apply_patch.py "TEN_FILE_GOC.bin" riot-stars-vi.rsvi "Ten khac.bin"
```

4. Đọc dòng cuối cùng mà lệnh in ra:

| Dòng cuối in ra | Nghĩa |
|---|---|
| `KHOP ban phat hanh` | Xong, đĩa đúng |
| `Dia goc khong dung (kich thuoc hoac sha256 khong khop)...` | Đĩa gốc sai, chưa ghi gì; xem mục 5 |
| `KHONG KHOP - hay bao loi kem sha256 dia goc` | Đĩa ra sai; xem mục 5 |
| `Khong phai file va Riot Stars (.rsvi).` | File `.rsvi` tải hỏng (thường là tải nhầm trang web); tải lại theo mục 0 |

## 4. Kiểm kết quả

Tính SHA-256 của file đã vá (cùng cách ở mục 2) và so với:

```
ec6b6862fc869741a70d793c77333e8a3a8dfec58b8a5c301db219157f47a2bc
```

Chỉ cần so 8 ký tự đầu (`ec6b6862`). Đúng chuỗi này thì file của bạn giống từng
byte với bản đã được kiểm thử; mọi lỗi nếu có sẽ không phải do bước áp vá.

`apply_patch.py` đã tạo sẵn file `.cue`. Nếu bạn đổi tên file `.bin` sau đó,
**kéo thả file `.bin` lên `tao_cue.bat`** (hoặc chép `tao_cue.bat` vào cùng thư
mục rồi nháy đúp) để tạo lại `.cue` đúng tên. Muốn làm tay thì tạo file văn bản
cùng tên với file `.bin` nhưng đuôi `.cue`, nội dung ba dòng, dòng đầu ghi
**đúng tên file `.bin`** của bạn:

```
FILE "Riot Stars (VN).bin" BINARY
  TRACK 01 MODE2/2352
    INDEX 01 00:00:00
```

## 5. Khi SHA-256 không khớp

- **Ảnh gốc ra chuỗi khác `18a138b6…`:** ảnh đĩa của bạn không phải bản mà bản
  vá được tạo từ đó. Nguyên nhân hay gặp: đọc đĩa ra kiểu `.iso` 2048 byte
  (kích thước sẽ nhỏ hơn 145 MB nhiều), đọc thiếu hoặc thừa sector cuối, đĩa
  thuộc bản in khác, hoặc file từng bị áp một bản vá khác. Cách chắc nhất là
  đọc lại từ đĩa thật bằng ImgBurn ở chế độ BIN/CUE.
- **Ảnh đã vá không khớp `ec6b6862…`:** file `.rsvi` tải hỏng hoặc không phải
  bản mới nhất; tải lại và áp lên bản gốc.

## 6. Chạy trên giả lập

Mở file **`.cue`** (không phải `.bin`) bằng giả lập. Đã chạy thử trên
DuckStation và PCSX-Redux; ePSXe, Mednafen/Beetle PSX đều đọc được BIN/CUE.

- **Không có BIOS gốc:** DuckStation chạy được với OpenBIOS (BIOS mã nguồn mở
  đi kèm PCSX-Redux): đặt file `openbios.bin` vào thư mục BIOS của DuckStation
  và chọn nó cho vùng NTSC-J.
- Thẻ nhớ (save trong game) dùng bình thường, kể cả thẻ từ bản Nhật.
- **Không nạp save state** (lưu nhanh của giả lập, kiểu F5/F7) được tạo trên
  bản Nhật: save state giữ nguyên toàn bộ bộ nhớ lúc lưu, nên vẫn hiện chữ cũ
  dù đĩa mới đã đúng. Vào game bằng "Chơi tiếp" từ thẻ nhớ.
- Màn nhập tên dùng bảng chữ Latin (A–Z, a–z, số, vài dấu câu).
- Phim mở đầu không bỏ qua được bằng START; chờ phim hết là tới màn tựa.

## 7. Những gì đã Việt hoá

- Toàn bộ lời thoại phần phiêu lưu và các trận đánh, tên nhân vật, lớp, vật
  phẩm, kỹ năng, phép, menu, hộp thoại, thông báo thẻ nhớ.
- Sòng bạc và đua ngựa: lời thoại, menu, tên ngựa.
- Chữ vẽ sẵn trên menu bản đồ và dòng chữ chạy ở trường đua.
- Phông chữ có dấu, rộng hẹp theo từng chữ (VWF).

Giới hạn:

- Cửa sổ trạng thái trong trận dùng phông nhỏ của máy, vốn chỉ có chữ hoa không
  dấu, nên tên đơn vị, lớp, vật phẩm ở đó viết HOA không dấu.
- Dòng chữ chạy ở trường đua cao 8 điểm ảnh nên viết không dấu.
- Tên nhân viên trong phần credit ở phim cuối game là chữ in sẵn trong video,
  giữ nguyên.

## 8. Câu hỏi thường gặp

**Sao không dùng PPF như các bản vá PS1 khác?** Chữ tiếng Việt dài hơn chữ
Nhật, nên vài file được dời về cuối đĩa. PPF chỉ ghi từng byte, nên bản vá PPF
sẽ phải chứa nguyên các file đó, tức là phát tán dữ liệu game. File `.rsvi` chỉ
ghi "sector này lấy từ sector nào của đĩa gốc" cộng phần chữ Việt, nên gói vá
không chứa dữ liệu game. Đổi lại cần Python để áp.

**Tại sao phải kiểm SHA-256 kỹ vậy?** Vì các lỗi khó chịu nhất (đứng máy, chữ
lỗi) thường bắt nguồn từ chỉ vài byte lệch. Kiểm hash là cách duy nhất biết
chắc file của bạn giống file đã được thử.

**Báo lỗi ở đâu?** Mở issue trên repo này, kèm: SHA-256 của file đã vá, tên
giả lập, và ảnh chụp màn hình cùng câu thoại cuối cùng trước khi lỗi.

## 9. Bản quyền

Trò chơi, tên gọi, hình ảnh và âm thanh thuộc Hect và các chủ sở hữu liên
quan. Bản vá chỉ chứa phần chữ dịch, phông chữ vẽ lại và các byte mã điều
chỉnh, không phân phối dữ liệu gốc. Nếu chủ sở hữu bản quyền yêu cầu, bản vá
sẽ được gỡ.

---

Bản dịch do **Khuong Doan** thực hiện — <https://khuongdoan.com/>

<sub>Bản vá miễn phí và sẽ luôn như vậy. Nếu nó giúp bạn chơi lại trò chơi tuổi thơ và bạn muốn mời tác giả một ly cà phê, quét mã MoMo bên dưới. Không bắt buộc, không kèm quyền lợi gì thêm.</sub>

<a href="https://github.com/2ez4gcx/Project-hub/blob/main/docs/anh/ung-ho-momo.png"><img src="https://raw.githubusercontent.com/2ez4gcx/Project-hub/main/docs/anh/ung-ho-momo.png" alt="Ủng hộ tác giả qua MoMo" width="170"></a>
