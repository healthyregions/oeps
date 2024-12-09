import { useState, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm'
import styles from "./RemoteMarkdownModal.module.css";

const fetchMarkdown = async (url) => await fetch(url).then(r => r.text()).then(r => r.replace('[here](/data_final).', '[here](/download).'))

export default function RemoteMarkdownModal({
    url=false,
    reset=() => {}
}){
    const [markdownText, setMarkdownText] = useState('')
    const [loading, setLoading] = useState(false)

    useEffect(() => {
        try {
            setLoading(true)
            fetchMarkdown(url).then(result => {setMarkdownText(result); setLoading(false)})
        } catch(e) {
            console.log(e)
        }
    },[url])

    return <div className={styles.fullScreenModal}>
        <button onClick={reset} className={styles.reset}>
            <span>
                ×
            </span>
        </button>
        <div className={styles.modalContainer}>
            {loading ? 
                <em>loading...</em> :
                <ReactMarkdown remarkPlugins={[remarkGfm]}>{markdownText}</ReactMarkdown>
            }
        </div>
    </div>
}
