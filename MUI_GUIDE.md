# MUI (Material-UI) 사용 가이드

## 설치 완료

다음 패키지가 설치되었습니다:
- `@mui/material` - MUI 핵심 컴포넌트
- `@emotion/react` - CSS-in-JS (필수 의존성)
- `@emotion/styled` - Styled components (필수 의존성)
- `@mui/icons-material` - Material Design 아이콘

## 기본 설정

`src/index.js`에 ThemeProvider와 CssBaseline이 추가되었습니다:
- **ThemeProvider**: 전역 테마 설정
- **CssBaseline**: 브라우저 기본 스타일 초기화

## 사용 가능한 주요 컴포넌트

### Layout
- `Container` - 반응형 컨테이너
- `Grid` - 그리드 레이아웃
- `Box` - 범용 박스 컴포넌트
- `Stack` - 수직/수평 스택 레이아웃
- `Paper` - 그림자 효과가 있는 표면

### Inputs
- `Button` - 버튼
- `TextField` - 텍스트 입력
- `Select` - 드롭다운 선택
- `Checkbox` - 체크박스
- `Radio` - 라디오 버튼
- `Switch` - 스위치

### Navigation
- `AppBar` - 상단 앱바
- `Drawer` - 사이드 메뉴
- `Tabs` - 탭
- `BottomNavigation` - 하단 네비게이션

### Data Display
- `Card` - 카드
- `List` - 리스트
- `Table` - 테이블
- `Chip` - 칩/태그
- `Badge` - 배지
- `Avatar` - 아바타

### Feedback
- `Alert` - 알림
- `Snackbar` - 토스트 메시지
- `Dialog` - 다이얼로그/모달
- `CircularProgress` - 로딩 스피너
- `LinearProgress` - 진행 바

### Icons
- `@mui/icons-material`에서 수천 개의 아이콘 사용 가능

## 사용 예시

### 1. Button 사용
```jsx
import Button from '@mui/material/Button';

<Button variant="contained" color="primary">
  클릭
</Button>
```

### 2. TextField 사용
```jsx
import TextField from '@mui/material/TextField';

<TextField
  label="이메일"
  variant="outlined"
  fullWidth
/>
```

### 3. Card 사용
```jsx
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';

<Card>
  <CardContent>
    <Typography variant="h5">제목</Typography>
    <Typography variant="body2">내용</Typography>
  </CardContent>
</Card>
```

### 4. Grid 레이아웃
```jsx
import Grid from '@mui/material/Grid';

<Grid container spacing={2}>
  <Grid item xs={12} md={6}>
    <div>왼쪽</div>
  </Grid>
  <Grid item xs={12} md={6}>
    <div>오른쪽</div>
  </Grid>
</Grid>
```

### 5. AppBar 사용
```jsx
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';

<AppBar position="static">
  <Toolbar>
    <Typography variant="h6">
      앱 제목
    </Typography>
  </Toolbar>
</AppBar>
```

### 6. Icon 사용
```jsx
import RestaurantIcon from '@mui/icons-material/Restaurant';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';

<RestaurantIcon />
<ShoppingCartIcon color="primary" />
```

### 7. Dialog 사용
```jsx
import Dialog from '@mui/material/Dialog';
import DialogTitle from '@mui/material/DialogTitle';
import DialogContent from '@mui/material/DialogContent';
import DialogActions from '@mui/material/DialogActions';
import Button from '@mui/material/Button';

<Dialog open={open} onClose={handleClose}>
  <DialogTitle>제목</DialogTitle>
  <DialogContent>내용</DialogContent>
  <DialogActions>
    <Button onClick={handleClose}>취소</Button>
    <Button onClick={handleConfirm}>확인</Button>
  </DialogActions>
</Dialog>
```

## 테마 커스터마이징

`src/index.js`에서 테마를 수정할 수 있습니다:

```jsx
const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2', // 메인 색상
    },
    secondary: {
      main: '#dc004e', // 보조 색상
    },
  },
  typography: {
    fontFamily: [
      '-apple-system',
      'BlinkMacSystemFont',
      '"Segoe UI"',
      'Roboto',
      '"Helvetica Neue"',
      'Arial',
      'sans-serif',
    ].join(','),
  },
});
```

## 반응형 디자인

MUI는 기본적으로 반응형을 지원합니다:

- `xs` - 모바일 (0px+)
- `sm` - 태블릿 (600px+)
- `md` - 데스크톱 (900px+)
- `lg` - 대형 데스크톱 (1200px+)
- `xl` - 초대형 화면 (1536px+)

```jsx
<Grid item xs={12} sm={6} md={4}>
  {/* 모바일: 전체, 태블릿: 절반, 데스크톱: 1/3 */}
</Grid>
```

## 유용한 링크

- 공식 문서: https://mui.com/material-ui/getting-started/
- 컴포넌트 목록: https://mui.com/material-ui/all-components/
- 아이콘 검색: https://mui.com/material-ui/material-icons/
- 예제: https://mui.com/material-ui/getting-started/templates/

## 다음 단계

1. 기존 컴포넌트를 MUI로 리팩토링
2. 일관된 디자인 시스템 적용
3. 반응형 레이아웃 개선
4. 접근성 향상

---

**생성일**: 2026-02-04T14:36:58+09:00
