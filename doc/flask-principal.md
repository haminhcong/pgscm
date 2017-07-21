# Authentication In Flask Application With Flask-Principal

Flask Principal sử dụng 4 khái niệm **Identity**, **Need**, **Permission** và **Identity Context** để xác thực và phân quyền các API-view.

**Identity** Object là đối tượng đại diện cho một Account trong quá trình thực hiện việc quá trình phân quyền. 

**Permission** Object là đối tượng đại diện cho quyền truy cập vào một tài nguyên nào đó trên hệ thống. Ví dụ: Trên hệ thống có 4 tài nguyên là Index View, Update View, Create View và Delete View thì chúng ta có thể sinh ra 4 permission đại diện cho quyền truy cập vào 4 View trên là IndexPermission, UpdatePermission, CreatePermisison và DeletePermission. Mỗi Permission Object sẽ có một phương thức validate(Identity) để xác định một Identity Object có thể đáp ứng (validate_result=True) được Permission đó không, tức là xác định Identity đó có được truy cập vào tài nguyên mà Permssion Object đó đang bảo vệ không. Để thực hiện được phương thức Validate, Permission có chứa các **Need**, được coi là đối tượng đơn vị trong thao tác phân quyền.

**Need** Object là đối tượng đơn vị cho một thao tác phân quyền. Need có thể là một đối tượng có 1,2 hay n thuộc tính, ví dụ như

- Need("role","admin") => Need này có nghĩa là "Có role là admin"
- Need("blog\_post","edit","15",) => Need này có nghĩa là Có quyền chỉnh sửa đối tượng blog\_post có id=15
- Need("role","admin","create_user") => Need này có nghĩa là có role là admin và có quyền tạo người dùng

Một Need tượng trưng cho việc được phép truy cập vào một tài nguyên nào đó trên hệ thống.

**IdentityContext** Object là context của một Identity Object xác định đối với một Permission Object xác định. Một Identity Context Object được khởi tạo với 2 parameter là (Identity\_Object\_x,Permission\_Object\_y). Identity Context này cho phép xác định Identity x có được truy cập vào tài nguyên do Permission y đại diện hay không. Nó xác định được chính là nhờ khái niệm **Need**, cụ thể:

- Một Permssion Object chứa một hoặc nhiều **Need**
- Một Identity Object có một hoặc nhiều **Need**

Identity context sẽ kiểm tra xem Permission y có chứa các Need nào, và kiểm tra xem danh sách các Need của Identity x có chứa một trong các Need đó không (1) . Nếu điều kiện (1) thỏa mãn, thì Identity x được truy cập vào các tài nguyên mà Permission x đang bảo vệ.

Ví dụ: 

- Identity x chứa các Need: (a1, a2, a3)
- Permission y có các Need (b1, b2, b3)
- Permission z có các Need (a1, c2, c3)

Thì x có thể truy cập vào các tài nguyên (các view,API) mà z bảo vệ, còn x không truy cập vào được cái tài nguyên do y bảo vệ, do x thỏa mãn chứa một trong các Need của z (a1).