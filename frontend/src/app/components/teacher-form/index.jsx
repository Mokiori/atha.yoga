import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import {
  Grid, Box, Typography, TextField, FormControl, RadioGroup, FormControlLabel, Radio,
  Button, Stack,
} from '@mui/material';
import { DesktopDatePicker, LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import TodayIcon from '@mui/icons-material/Today';
import 'dayjs/locale/ru';
import UploadFiles from '../upload_files';
import postQuestionnaireSlice from '../../core/slices/questionnaire/postQuestionnaire';
import { clearMessage } from '../../core/slices/message';

const TeacherForm = () => {
  const [answers, setAnswers] = useState({
    name: '',
    surname: '',
    date_of_birth: null,
    gender: '',
    about_me: '',
    work_experience: '',
    vk_link: '',
    telegram_link: '',
    certificate_photos: [],
    passport_photo: null,
    user_photo: null,
    user_with_passport_photo: null,
  });

  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(clearMessage());
  }, []);

  const { message } = useSelector(state => state.message);

  const [photos, setPhoto] = useState([]);

  const updateCertificate = files => {
    setPhoto([...photos, ...files]);
  };

  const updatePhoto = (file, nameLoader) => {
    setAnswers({ ...answers, [nameLoader]: file });
  };

  const handleChangeAnswer = prop => event => {
    setAnswers({ ...answers, [prop]: event.target.value });
  };

  const postAnswers = answersArr => {
    const dateOfBirth = answersArr.date_of_birth;
    dispatch(postQuestionnaireSlice({
      ...answersArr,
      certificate_photos: photos,
      date_of_birth: dateOfBirth ? `${dateOfBirth.$y}-${dateOfBirth.$M + 1}-${dateOfBirth.$D}` : null,
    }));
  };

  const handleChangeDate = newValue => {
    setAnswers({ ...answers, date_of_birth: newValue });
  };

  const isEmpty = () => Object.values(answers).includes('') || Object.values(answers).includes(null) || !photos.length;

  return (
    <Box sx={{ maxWidth: '732px', width: '100%' }}>
      <Typography fontWeight="600" fontSize="24px" mb="34px">
        Заполните анкету
      </Typography>
      <Typography color="text.secondary" mb="24px">
        * Поля, обязательные для заполнения
      </Typography>
      <Grid container spacing="24px" mb="60px">
        <Grid item xs={12} sm={6}>
          <TextField
            fullWidth
            required
            id="first-name"
            label="Имя"
            onChange={handleChangeAnswer('name')}
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            fullWidth
            required
            id="surname"
            label="Фамилия"
            onChange={handleChangeAnswer('surname')}
          />
        </Grid>
        <Grid item xs={12}>
          <LocalizationProvider adapterLocale="ru" dateAdapter={AdapterDayjs}>
            <Stack>
              <DesktopDatePicker
                label="День рождения *"
                inputFormat="DD.MM.YYYY"
                value={answers.date_of_birth}
                onChange={handleChangeDate}
                renderInput={params => <TextField {...params} />}
                components={{
                  OpenPickerIcon: TodayIcon,
                }}
              />
            </Stack>
          </LocalizationProvider>
        </Grid>
        <Grid item>
          <FormControl>
            <RadioGroup row onChange={handleChangeAnswer('gender')}>
              <FormControlLabel
                value="MALE"
                control={<Radio />}
                label="мужчина"
              />
              <FormControlLabel
                value="FEMALE"
                control={<Radio />}
                label="женщина"
              />
            </RadioGroup>
          </FormControl>
        </Grid>
        <Grid item xs={12}>
          <TextField
            fullWidth
            required
            multiline
            label="О себе"
            id="about-me"
            rows={8}
            helperText="Не более 3000 символов"
            inputProps={{ maxLength: 3000 }}
            onChange={handleChangeAnswer('about_me')}
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            fullWidth
            required
            multiline
            label="Опыт работы"
            id="work-experience"
            rows={6}
            helperText="Не более 1000 символов"
            inputProps={{ maxLength: 1000 }}
            onChange={handleChangeAnswer('work_experience')}
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            fullWidth
            required
            id="vk-link"
            label="Ссылка на страницу ВК"
            onChange={handleChangeAnswer('vk_link')}
            error={!!message?.invalid?.vk_link}
            helperText={message?.invalid?.vk_link}
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <TextField
            fullWidth
            required
            id="telegram-link"
            label="Ссылка на профиль в Telegram"
            onChange={handleChangeAnswer('telegram_link')}
            error={!!message?.invalid?.telegram_link}
            helperText={message?.invalid?.telegram_link}
          />
        </Grid>
        <Grid item xs={12}>
          <Typography sx={{ fontSize: '18px', fontWeight: '600', mb: '16px' }}>Фото пользователя</Typography>
          <UploadFiles updatePhoto={updatePhoto} loaderName="user_photo" />
        </Grid>
        <Grid item xs={12}>
          <Typography sx={{ fontSize: '18px', fontWeight: '600', mb: '16px' }}>Фото паспорта</Typography>
          <UploadFiles updatePhoto={updatePhoto} loaderName="passport_photo" />
        </Grid>
        <Grid item xs={12}>
          <Typography sx={{ fontSize: '18px', fontWeight: '600', mb: '16px' }}>
            Фото пользователя с паспортом
          </Typography>
          <UploadFiles updatePhoto={updatePhoto} loaderName="user_with_passport_photo" />
        </Grid>
        <Grid item xs={12}>
          <Typography sx={{ fontSize: '18px', fontWeight: '600', mb: '16px' }}>
            Документы, подтверждающие квалификацию и опыт работы
          </Typography>
          <UploadFiles updateCertificate={updateCertificate} loaderName="certificate_photos" />
        </Grid>
      </Grid>
      <Box
        display="flex"
        flexDirection="column"
        alignItems="flex-end"
        gap="30px"
      >
        <Box sx={{ maxWidth: '311px', width: '100%' }}>
          <Button
            fullWidth
            variant="contained"
            disabled={isEmpty()}
            size="large"
            onClick={() => postAnswers(answers)}
          >
            Отправить на проверку
          </Button>
        </Box>
        <Box display="flex" sx={{ maxWidth: '311px' }}>
          <Typography fontSize="12px" fontWeight="400" textAlign="center">
            Отправляя форму, вы соглашаетесь с
            <Typography
              component="span"
              fontSize="12px"
              fontWeight="400"
              color="primary"
            >
              {' '}
              офертой
            </Typography>
            {' '}
            и даёте согласие на
            <Typography
              component="span"
              fontSize="12px"
              fontWeight="400"
              color="primary"
            >
              {' '}
              обработку ваших персональных данных
            </Typography>
          </Typography>
        </Box>
      </Box>
    </Box>
  );
};

export default TeacherForm;
