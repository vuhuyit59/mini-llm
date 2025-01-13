import React, {useEffect, useState} from 'react';
import {GetServerSideProps} from 'next';
import Layout from '@/components/Layout/Layout';
import Box from "@mui/material/Box";
import {Button, CircularProgress, TextField} from '@mui/material';
import styles from '@/styles/Home.module.scss';
import {useMutation, useQuery} from 'react-query';
import {
    getAiVideoRequestDetail,
    createAiVideoRequest
} from '@/helpers/api/aiVideoRequest';
import toast from "react-hot-toast";
import {useCountdown} from 'usehooks-ts'

export default function Home() {
    const userId = "user1"
    const [inputText, setInputText] = useState('');
    const [disableSendBtn, setDisableSendBtn] = useState(false);
    const [currentAiVideoRequestId, setCurrentAiVideoRequestId] = useState(null);
    const [count, {startCountdown, stopCountdown, resetCountdown}] =
        useCountdown({
            countStart: 30,
            intervalMs: 1000,
        })

    const {
        data: currentAiVideoRequestData,
        refetch: refetchAiVideoRequestDetail
    } = useQuery(
        ['getPrompts', userId, currentAiVideoRequestId],
        () => getAiVideoRequestDetail(userId, currentAiVideoRequestId || ''),
        {
            enabled: currentAiVideoRequestId !== null,
        }
    );
    const {
        mutate: createAiVideoRequestFunc,
    } = useMutation(createAiVideoRequest, {
        onSuccess: (data) => {
            setCurrentAiVideoRequestId(data.data?.id);
            setDisableSendBtn(true);
            startCountdown();
        },
        onError: () => {
            alert('Create ai video request failed !!!');
        },
    });

    const handleSubmit = () => {
        const payload = {
            input_sample: inputText,
            user_id: userId,
        };
        if (!payload.input_sample) {
            toast.error('Invalid input', {position: 'bottom-center'})
            return;
        }
        createAiVideoRequestFunc(payload);
    };

    useEffect(() => {
        if (currentAiVideoRequestData?.data?.status && currentAiVideoRequestData?.data?.status !== "PROCESSING") {
            setDisableSendBtn(false);
            stopCountdown();
            resetCountdown();
        }
    }, [currentAiVideoRequestData])

    useEffect(() => {
        if (count === 0 && disableSendBtn) {
            resetCountdown();
            startCountdown();
            refetchAiVideoRequestDetail();
        }
    }, [count])

    console.log(count)

    return (
        <Layout>
            <div className={styles.wrapper}>
                <div className={styles.chatWrapper}>
                    {
                        currentAiVideoRequestData ? (
                            <div>
                                <div className={styles.labelWrapper}>
                                    <h3>Ai video request
                                        status: {currentAiVideoRequestData?.data?.status}</h3>
                                    {currentAiVideoRequestData?.data?.status === "PROCESSING" ? (
                                        <div className={styles.labelWrapper}>
                                            <CircularProgress/>
                                            <h3
                                                className={styles.processCircularPercent}>{currentAiVideoRequestData?.data?.process_percent || 0}%
                                            </h3>
                                        </div>) : null}
                                </div>
                                {currentAiVideoRequestData?.data?.image_url ? (
                                    <div>
                                        <h3>Visual representations of the
                                            concept</h3>
                                        <div>
                                            <img className={styles.imgWrapper}
                                                 src={currentAiVideoRequestData?.data?.image_url}
                                                 alt=""/>
                                        </div>
                                    </div>
                                ) : null}
                                {currentAiVideoRequestData?.data?.output_video_url ? (
                                    <div>
                                        <h3>Ai video</h3>
                                        <div>
                                            <video
                                                controls
                                                className={styles.videoWrapper}
                                                src={currentAiVideoRequestData?.data?.output_video_url}
                                                />
                                        </div>
                                    </div>
                                ) : null}
                            </div>
                        ) : null
                    }
                </div>
                <Box>
                    <div className={styles.chatBoxWrapper}>
                        <div className={styles.textInputWrapper}>
                            <TextField
                                margin="normal"
                                required
                                id="input_sample"
                                label="Video concept or script"
                                name="input_sample"
                                placeholder="Type your video concept, script, or description here. For example: 'A serene mountain sunrise with gentle music playing in the background."
                                autoFocus
                                className={styles.textInput}
                                minRows={6}
                                onChange={e => setInputText(e.target.value)}
                            />
                        </div>
                        <Button disabled={disableSendBtn} variant="contained"
                                onClick={handleSubmit}>
                            send
                        </Button>
                    </div>
                </Box>

            </div>
        </Layout>
    );
}

export const getServerSideProps: GetServerSideProps = async () => {
    return {
        props: {},
    };
};
